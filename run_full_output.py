"""
AgroCure AI - Comprehensive Trilingual & 5-Language Output Demonstration.
Demonstrates output across English, Hindi, Kannada, Marathi, and Tamil.
"""

from PIL import Image
from pathlib import Path
import json
from ai_engine.inference import agrocure_ai_engine

samples = [
    ("sample_pepper_bacterial_spot.jpg", "Pepper", "mr", "Marathi (मराठी)"),
    ("sample_wheat_stripe_rust.jpg", "Wheat", "ta", "Tamil (தமிழ்)"),
    ("sample_grapes_black_rot.jpg", "Grapes", "hi", "Hindi (हिंदी)"),
    ("sample_corn_common_rust.jpg", "Corn", "kn", "Kannada (ಕನ್ನಡ)"),
    ("sample_wheat_stripe_rust.jpg", "Wheat", "en", "English")
]

print("=" * 80)
print(" AGROCURE AI - 5-LANGUAGE COMPREHENSIVE OUTPUT DEMO")
print("=" * 80)

samples_dir = Path(__file__).resolve().parent / "static" / "samples"

for fname, crop, lang, lang_name in samples:
    img_path = samples_dir / fname
    img = Image.open(img_path)
    res = agrocure_ai_engine.predict(img, crop_hint=crop, lang=lang)
    
    p = res["prediction"]
    d = res["detection"]
    t = res["treatment"]

    print(f"\n[LANGUAGE: {lang_name.upper()} | CROP: {crop.upper()}]")
    print(f"File Tested:        {fname}")
    print(f"Identified Crop:    {p['localized_crop']}")
    print(f"Disease Diagnosis:  {p['localized_disease']}")
    print(f"Severity Rating:    {p['severity']}")
    print(f"AI Confidence:      {p['confidence']}%")
    print(f"Leaf Detected:      {d['is_leaf_detected']}")
    print(f"Bounding Box:       {d['bounding_box']}")
    print(f"Healthy Foliage:    {d['healthy_green_pct']}%")
    print(f"Lesion Area:        {d['lesion_pct']}%")
    print(f"Pathogen:           {p['pathogen']}")
    print(f"Visual Symptoms:    {t['symptoms']}")
    print(f"Organic Remedy:     {t['organic'][0]}")
    print(f"Chemical Spray:     {t['chemical'][0]}")
    print(f"Cultural Practices: {t['prevention'][0]}")
    print("-" * 80)

print("\n[SUCCESS] All 5 languages tested and functional!")
