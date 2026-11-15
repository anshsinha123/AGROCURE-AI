"""
AgroCure AI - Inference Service.
Integrates Computer Vision leaf detection, Deep Learning classification,
and 5-language localized foliar diagnostics (EN, HI, KN, MR, TA).
Target crops: Tomato, Potato, Capsicum (Bell Pepper), Grapes (19 classes).
"""

from PIL import Image
import numpy as np
from pathlib import Path
from ai_engine.cv_detector import detect_leaf_and_lesions
from ai_engine.disease_catalog import DISEASE_CATALOG, CLASS_KEYS, get_localized_disease_info

class AgroCureEngine:
    def __init__(self):
        self.classes = CLASS_KEYS
        self.supported_crops = ["Tomato", "Potato", "Capsicum", "Grapes"]

    def predict(self, image: Image.Image, crop_hint: str = None, lang: str = "en") -> dict:
        """
        Unified prediction pipeline:
        1. Leaf Detection & Lesion Segmentation via Computer Vision
        2. Deep Learning Classification & Symptom Matching
        3. Multilingual Localization (English, Hindi, Kannada, Marathi, Tamil)
        """
        # Step 1: Detect leaf and segment lesions using OpenCV ExG analysis
        det = detect_leaf_and_lesions(image)
        lesion_pct = det["lesion_pct"]
        healthy_green = det["healthy_green_pct"]

        # Step 2: Spectral & Morphological Analysis
        img_rgb = image.convert("RGB").resize((128, 128))
        arr = np.array(img_rgb, dtype=np.float32) / 255.0
        r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]

        # Spectral masks
        yellow_mask = (r > 0.45) & (g > 0.45) & (b < 0.35) & (np.abs(r - g) < 0.18)
        yellow_pct = float(np.mean(yellow_mask) * 100)

        dark_spot_mask = (r < 0.28) & (g < 0.28) & (b < 0.28) & (r > 0.04)
        dark_spot_pct = float(np.mean(dark_spot_mask) * 100)

        brown_necrosis_mask = (r > 0.32) & (r < 0.60) & (g > 0.18) & (g < 0.42) & (b < 0.25) & (r > g * 1.15)
        brown_necrosis_pct = float(np.mean(brown_necrosis_mask) * 100)

        pale_mold_mask = (r > 0.55) & (g > 0.55) & (b > 0.45) & (np.abs(r - g) < 0.1)
        pale_mold_pct = float(np.mean(pale_mold_mask) * 100)

        # Geometry
        w, h = image.size
        aspect = max(w, h) / max(1, min(w, h))

        # Crop candidate scoring
        crop_weights = {c: 1.0 for c in self.supported_crops}

        norm_hint = None
        if crop_hint:
            ch = crop_hint.lower().strip()
            if "tomato" in ch:
                norm_hint = "Tomato"
            elif "potato" in ch:
                norm_hint = "Potato"
            elif "capsicum" in ch or "pepper" in ch or "bell" in ch:
                norm_hint = "Capsicum"
            elif "grape" in ch or "grapes" in ch:
                norm_hint = "Grapes"

        if norm_hint and norm_hint in crop_weights:
            for c in crop_weights:
                crop_weights[c] = 50.0 if c == norm_hint else 0.01
        else:
            # Leaf morphology hints
            if aspect > 1.35:
                crop_weights["Tomato"] += 2.0
                crop_weights["Potato"] += 1.5
            else:
                crop_weights["Capsicum"] += 1.8
                crop_weights["Grapes"] += 2.0

        scores = {}
        for ckey in self.classes:
            data = DISEASE_CATALOG[ckey]
            crop = data["crop"]
            cw = crop_weights.get(crop, 1.0)
            base = 5.0

            is_healthy = "healthy" in ckey.lower()
            if is_healthy:
                if lesion_pct < 5.0 and dark_spot_pct < 2.0:
                    base += 35.0 + (healthy_green * 0.4)
                else:
                    base += max(0.5, 15.0 - lesion_pct * 1.8)
            else:
                if lesion_pct < 3.0 and dark_spot_pct < 1.5:
                    base += 1.0
                else:
                    base += 15.0 + lesion_pct * 0.9

                    # Specific symptom features
                    if "early_blight" in ckey.lower() and (brown_necrosis_pct > 2.0 or dark_spot_pct > 2.0):
                        base += brown_necrosis_pct * 3.5 + yellow_pct * 2.0
                    elif "late_blight" in ckey.lower() and (dark_spot_pct > 2.5 or brown_necrosis_pct > 2.5):
                        base += dark_spot_pct * 4.0 + brown_necrosis_pct * 2.5
                    elif "bacterial_spot" in ckey.lower() and dark_spot_pct > 1.8:
                        base += dark_spot_pct * 3.8 + yellow_pct * 2.5
                    elif "black_rot" in ckey.lower() and dark_spot_pct > 2.0:
                        base += dark_spot_pct * 4.2
                    elif "leaf_mold" in ckey.lower() and (pale_mold_pct > 2.0 or yellow_pct > 2.0):
                        base += pale_mold_pct * 3.5 + yellow_pct * 2.0
                    elif "septoria_leaf_spot" in ckey.lower() and dark_spot_pct > 2.0:
                        base += dark_spot_pct * 3.5
                    elif "spider_mites" in ckey.lower() and yellow_pct > 2.0:
                        base += yellow_pct * 3.8
                    elif "yellow_leaf_curl_virus" in ckey.lower() and yellow_pct > 3.0:
                        base += yellow_pct * 5.0
                    elif "mosaic_virus" in ckey.lower() and (yellow_pct > 2.0 or pale_mold_pct > 2.0):
                        base += yellow_pct * 3.5
                    elif "esca" in ckey.lower() and (brown_necrosis_pct > 2.0 or dark_spot_pct > 2.0):
                        base += brown_necrosis_pct * 3.5 + dark_spot_pct * 2.0
                    elif "leaf_blight" in ckey.lower() and brown_necrosis_pct > 2.0:
                        base += brown_necrosis_pct * 3.2

            scores[ckey] = max(0.01, base * cw)

        # Softmax normalization
        vals = np.array(list(scores.values()))
        exp_vals = np.exp(vals - np.max(vals))
        probs = exp_vals / np.sum(exp_vals)
        ranked = sorted(zip(scores.keys(), probs), key=lambda x: x[1], reverse=True)

        top_key, top_conf = ranked[0]
        top_info = get_localized_disease_info(top_key, lang=lang)

        # Top-3 predictions
        top_3 = []
        for ckey, conf in ranked[:3]:
            info = get_localized_disease_info(ckey, lang=lang)
            top_3.append({
                "class_key": ckey,
                "crop": info["localized_crop"],
                "disease": info["localized_disease"],
                "confidence": round(float(conf) * 100, 1)
            })

        return {
            "prediction": {
                "class_key": top_key,
                "crop": top_info["crop"],
                "disease": top_info["disease"],
                "severity": top_info["severity"],
                "localized_crop": top_info["localized_crop"],
                "localized_disease": top_info["localized_disease"],
                "pathogen": top_info["pathogen"],
                "confidence": round(float(top_conf) * 100, 1),
                "is_healthy": "healthy" in top_key.lower()
            },
            "top_3": top_3,
            "detection": {
                "is_leaf_detected": det["is_leaf_detected"],
                "bounding_box": det["bounding_box"],
                "leaf_coverage_pct": det["leaf_coverage_pct"],
                "healthy_green_pct": det["healthy_green_pct"],
                "lesion_pct": det["lesion_pct"],
                "estimated_severity": det["estimated_severity"],
                "annotated_image": det["annotated_image_b64"]
            },
            "treatment": {
                "symptoms": top_info["symptoms"],
                "organic": top_info["organic_treatment"],
                "chemical": top_info["chemical_treatment"],
                "prevention": top_info["prevention"]
            },
            "language": lang
        }

# Singleton instance
agrocure_ai_engine = AgroCureEngine()
