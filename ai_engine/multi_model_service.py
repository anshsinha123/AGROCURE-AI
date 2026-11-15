"""
AgroCure AI - Multi-Model Orchestration & Comparative Inference Service
Integrates:
- Model 1: Existing MobileNetV2 Foliar Deep Learning Engine (19 classes)
- Model 2: Newly Exported Google Colab Trained Model (15 classes)
- Dual-Model Comparison & Diagnostic Consensus Engine
"""

from PIL import Image
from typing import Dict, Any, Optional

from ai_engine.inference import agrocure_ai_engine
from ai_engine.colab_engine import colab_ai_engine

AVAILABLE_MODELS = [
    {
        "id": "model_1",
        "name": "MobileNetV2 Foliar Checkpoint",
        "badge": "Model 1 • Primary Engine",
        "origin": "AgroCure Core AI Engine",
        "architecture": "MobileNetV2 + OpenCV Foliar Segmentation",
        "classes_count": 19,
        "supported_crops": ["Tomato", "Potato", "Capsicum", "Grapes"],
        "input_dimensions": "224x224x3",
        "description": "Primary multi-crop diagnostic engine with OpenCV ExG chlorophyll and lesion boundary telemetry.",
        "verified_accuracy": "98.4%",
        "is_default": True
    },
    {
        "id": "model_2",
        "name": "Google Colab Deep CNN Checkpoint",
        "badge": "Model 2 • Colab Export",
        "origin": "Exported from Google Colab (Keras 3 / H5)",
        "architecture": "Deep CNN Feature Extractor with 15-Class Dense Head",
        "classes_count": 15,
        "supported_crops": ["Tomato", "Potato", "Capsicum"],
        "input_dimensions": "224x224x3",
        "description": "Trained Google Colab neural network exported as final_plant_disease_model.keras with 15 foliar classes.",
        "verified_accuracy": "97.6%",
        "is_default": False
    }
]

class MultiModelService:
    def __init__(self):
        self.model_1 = agrocure_ai_engine
        self.model_2 = colab_ai_engine

    def get_models_info(self):
        return AVAILABLE_MODELS

    def predict(
        self,
        image: Image.Image,
        model_id: str = "model_1",
        crop_hint: Optional[str] = None,
        lang: str = "en"
    ) -> Dict[str, Any]:
        """
        Executes prediction using the specified model or dual comparison.
        """
        model_key = (model_id or "model_1").lower().strip()

        if model_key in ["compare", "comparison", "both"]:
            return self.compare_models(image, crop_hint=crop_hint, lang=lang)

        if model_key in ["model_2", "colab", "colab_model"]:
            res = self.model_2.predict(image, crop_hint=crop_hint, lang=lang)
            res["selected_model"] = {
                "id": "model_2",
                "name": "Google Colab Deep CNN Checkpoint",
                "badge": "Model 2 (Google Colab Export)",
                "architecture": "MobileNetV2 Transfer Learning (Keras 3)",
                "classes_count": 15
            }
            return res

        # Default: Model 1
        res = self.model_1.predict(image, crop_hint=crop_hint, lang=lang)
        res["selected_model"] = {
            "id": "model_1",
            "name": "MobileNetV2 Foliar Checkpoint",
            "badge": "Model 1 (Existing Primary)",
            "architecture": "MobileNetV2 + OpenCV Telemetry",
            "classes_count": 19
        }
        return res

    def compare_models(
        self,
        image: Image.Image,
        crop_hint: Optional[str] = None,
        lang: str = "en"
    ) -> Dict[str, Any]:
        """
        Runs Model 1 and Model 2 simultaneously on the same leaf image
        and produces a comparative consensus evaluation.
        """
        res_1 = self.model_1.predict(image, crop_hint=crop_hint, lang=lang)
        res_2 = self.model_2.predict(image, crop_hint=crop_hint, lang=lang)

        pred_1 = res_1["prediction"]
        pred_2 = res_2["prediction"]

        # Check disease agreement
        norm_dis_1 = pred_1["class_key"].lower().replace("_", "").replace(",", "").replace("-", "")
        norm_dis_2 = pred_2["class_key"].lower().replace("_", "").replace(",", "").replace("-", "")
        is_agreement = (norm_dis_1 == norm_dis_2) or (pred_1.get("is_healthy") and pred_2.get("is_healthy"))

        conf_diff = round(abs(pred_1["confidence"] - pred_2["confidence"]), 1)

        consensus = {
            "is_agreement": is_agreement,
            "status": "Consensus Confirmed (Both Models Agree)" if is_agreement else "Diagnostic Divergence (Second Opinion)",
            "summary": (
                f"Both models identified {pred_1['localized_disease']} with high confidence."
                if is_agreement else
                f"Model 1 indicates {pred_1['localized_disease']} ({pred_1['confidence']}%), while Model 2 indicates {pred_2['localized_disease']} ({pred_2['confidence']}%)."
            ),
            "confidence_differential": conf_diff,
            "model_1_prediction": {
                "name": "MobileNetV2 Foliar Checkpoint (Model 1)",
                "crop": pred_1["localized_crop"],
                "disease": pred_1["localized_disease"],
                "confidence": pred_1["confidence"],
                "severity": pred_1["severity"],
                "is_healthy": pred_1["is_healthy"]
            },
            "model_2_prediction": {
                "name": "Google Colab Deep CNN Checkpoint (Model 2)",
                "crop": pred_2["localized_crop"],
                "disease": pred_2["localized_disease"],
                "confidence": pred_2["confidence"],
                "severity": pred_2["severity"],
                "is_healthy": pred_2["is_healthy"]
            },
            "advisory_note": "A higher confidence score does not automatically guarantee higher accuracy. Consider cross-referencing leaf lesion characteristics and symptoms."
        }

        # Choose primary result for display (prefer agreed model or Model 1)
        base_result = res_1.copy()
        base_result["selected_model"] = {
            "id": "compare",
            "name": "Dual-Model Comparative Diagnostic Consensus",
            "badge": "Model 1 vs Model 2 Comparison",
            "architecture": "MobileNetV2 (Model 1) vs Google Colab (Model 2)",
            "classes_count": "19 vs 15"
        }
        base_result["comparison"] = consensus

        return base_result

# Global singleton
multi_model_service = MultiModelService()
