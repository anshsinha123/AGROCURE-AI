"""
AgroCure AI - Second Trained Machine Learning Model (Google Colab Export)
Inference Service for Google Colab Trained Model (final_plant_disease_model.keras).
Input Dimensions: 224x224x3
Supported Classes: 15 foliar classes across Tomato, Potato, and Capsicum (Bell Pepper).
"""

import json
import numpy as np
from pathlib import Path
from PIL import Image

from ai_engine.cv_detector import detect_leaf_and_lesions
from ai_engine.disease_catalog import CLASS_KEYS, get_localized_disease_info

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"
MODEL_PATH = MODELS_DIR / "final_plant_disease_model.keras"
CLASS_NAMES_PATH = MODELS_DIR / "class_names.json"


class ModelUnavailableError(RuntimeError):
    """Raised when the Colab checkpoint cannot be loaded for inference."""


class ColabModelEngine:
    def __init__(self):
        self.model_name = "Google Colab Deep Learning Checkpoint"
        self.model_id = "model_2"
        self.model_architecture = "MobileNetV2 Transfer Learning (Keras 3)"
        self.input_shape = (224, 224, 3)
        self.class_names = []
        self.class_mapping = {}
        self.keras_model = None
        self.is_loaded = False
        self.load_error = None

        self._load_class_names()
        self._initialize_model()

    def _load_class_names(self):
        """Loads and maps the 15 class names exported from Google Colab."""
        if CLASS_NAMES_PATH.exists():
            try:
                with open(CLASS_NAMES_PATH, "r", encoding="utf-8") as f:
                    self.class_names = json.load(f)
            except Exception as e:
                print(f"[ColabEngine] Error reading class_names.json: {e}")

        if not self.class_names:
            # Fallback default 15 Colab classes
            self.class_names = [
                'Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy',
                'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
                'Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight',
                'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot',
                'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot',
                'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus',
                'Tomato_healthy'
            ]

        # Map Colab class names to AgroCure DISEASE_CATALOG keys
        def norm(k):
            return k.lower().replace("_", "").replace(",", "").replace("-", "").replace(" ", "")

        for colab_name in self.class_names:
            norm_c = norm(colab_name)
            matched = None
            for cat_key in CLASS_KEYS:
                if norm_c == norm(cat_key):
                    matched = cat_key
                    break
            if not matched:
                # Approximate fallback
                for cat_key in CLASS_KEYS:
                    if colab_name.split("_")[0].lower() in cat_key.lower():
                        matched = cat_key
                        break
            self.class_mapping[colab_name] = matched or "Tomato___Early_blight"

    def _initialize_model(self):
        """Loads the complete trained Keras model used by Model 2."""
        if not MODEL_PATH.exists():
            self.load_error = f"Model checkpoint not found: {MODEL_PATH}"
            print(f"[ColabEngine] {self.load_error}")
            return

        try:
            import keras
            model = keras.models.load_model(str(MODEL_PATH), compile=False)
            output_shape = model.output_shape
            if isinstance(output_shape, list) or output_shape[-1] != len(self.class_names):
                raise ValueError(
                    f"Checkpoint output shape {output_shape} does not match "
                    f"{len(self.class_names)} configured classes."
                )
            self.keras_model = model
            self.is_loaded = True
            print("[ColabEngine] Successfully loaded Google Colab model via Keras!")
        except Exception as e:
            self.load_error = f"Unable to load Model 2 checkpoint: {e}"
            print(f"[ColabEngine] {self.load_error}")

    def preprocess_image(self, image: Image.Image) -> np.ndarray:
        """
        Preprocesses image for the Google Colab model:
        1. Resize to (224, 224)
        2. Convert to RGB float32 in the 0-255 range
        3. The saved model applies MobileNetV2 normalization internally
        """
        img_resized = image.convert("RGB").resize((self.input_shape[0], self.input_shape[1]), Image.Resampling.BILINEAR)
        arr = np.array(img_resized, dtype=np.float32)
        return np.expand_dims(arr, axis=0)

    def predict(self, image: Image.Image, crop_hint: str = None, lang: str = "en") -> dict:
        """
        Performs plant disease prediction using the second (Colab) trained model.
        Returns standardized diagnostics, confidence scores, and localized treatments.
        """
        if not self.is_loaded or self.keras_model is None:
            raise ModelUnavailableError(
                self.load_error or "Model 2 is unavailable. Install the project requirements and restart the server."
            )

        # Step 1: Computer Vision foliar inspection & lesion boundary detection
        det = detect_leaf_and_lesions(image)

        # Step 2: Run the complete trained network and validate its class output.
        input_tensor = self.preprocess_image(image)
        predictions = np.asarray(self.keras_model.predict(input_tensor, verbose=0))
        if predictions.shape != (1, len(self.class_names)):
            raise RuntimeError(
                f"Model 2 returned output shape {predictions.shape}; "
                f"expected (1, {len(self.class_names)})."
            )
        probs = predictions[0].astype(np.float64)
        if not np.all(np.isfinite(probs)) or np.any(probs < 0) or probs.sum() <= 0:
            raise RuntimeError("Model 2 returned invalid class probabilities.")
        probs /= probs.sum()

        # Apply crop filter weighting if user provided crop hint
        if crop_hint and crop_hint.lower() not in ["auto-detect", "all", ""]:
            ch = crop_hint.lower().strip()
            for i, cname in enumerate(self.class_names):
                first_part = cname.split("_")[0].lower()
                if ch in first_part or ("capsicum" in ch and "pepper" in first_part) or ("pepper" in ch and "pepper" in first_part):
                    probs[i] *= 25.0
                else:
                    probs[i] *= 0.05
            probs = probs / np.sum(probs)

        # Rank predictions
        ranked = sorted(zip(self.class_names, probs), key=lambda x: x[1], reverse=True)
        top_colab_name, top_prob = ranked[0]
        top_cat_key = self.class_mapping.get(top_colab_name, "Tomato___Early_blight")
        top_info = get_localized_disease_info(top_cat_key, lang=lang)

        conf_pct = round(float(top_prob) * 100, 1)

        # Top-3 predictions
        top_3 = []
        for cname, pval in ranked[:3]:
            mapped_key = self.class_mapping.get(cname, "Tomato___Early_blight")
            info = get_localized_disease_info(mapped_key, lang=lang)
            c_conf = round(float(pval) * 100, 1)
            top_3.append({
                "class_key": mapped_key,
                "colab_class": cname,
                "crop": info["localized_crop"],
                "disease": info["localized_disease"],
                "confidence": c_conf
            })

        is_healthy = "healthy" in top_colab_name.lower() or "healthy" in top_cat_key.lower()

        return {
            "prediction": {
                "class_key": top_cat_key,
                "colab_class": top_colab_name,
                "crop": top_info["crop"],
                "disease": top_info["disease"],
                "severity": top_info["severity"] if not is_healthy else "None",
                "localized_crop": top_info["localized_crop"],
                "localized_disease": top_info["localized_disease"],
                "pathogen": top_info["pathogen"],
                "confidence": conf_pct,
                "is_healthy": is_healthy,
                "model_name": self.model_name,
                "model_id": self.model_id,
                "model_architecture": self.model_architecture,
                "input_dimensions": "224x224x3",
                "total_supported_classes": len(self.class_names)
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

# Singleton instance for Second Model
colab_ai_engine = ColabModelEngine()
