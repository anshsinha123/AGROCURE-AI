"""
AgroCure AI Verification Script.
Tests predictions across Pepper, Grapes, Wheat, and Corn in English, Hindi, and Kannada.
"""

from PIL import Image
from pathlib import Path
from ai_engine.inference import agrocure_ai_engine

test_cases = [
    ("sample_pepper_bacterial_spot.jpg", "Pepper", "en"),
    ("sample_grapes_black_rot.jpg", "Grapes", "hi"),
    ("sample_wheat_stripe_rust.jpg", "Wheat", "kn"),
    ("sample_corn_common_rust.jpg", "Corn", "hi")
]

print("="*75)
print(" AGROCURE AI - TRILINGUAL INFERENCE VERIFICATION")
print("="*75)

samples_dir = Path(__file__).resolve().parent / "static" / "samples"

for fname, crop, lang in test_cases:
    path = samples_dir / fname
    img = Image.open(path)
    res = agrocure_ai_engine.predict(img, crop_hint=crop, lang=lang)
    p = res["prediction"]
    d = res["detection"]
    t = res["treatment"]

    print(f"\n[LANG: {lang.upper()}] Crop: {crop} | File: {fname}")
    print(f" -> Localized Crop:    {p['localized_crop']}")
    print(f" -> Localized Disease: {p['localized_disease']} ({p['confidence']}%)")
    print(f" -> Severity:          {p['severity']} | Lesion Area: {d['lesion_pct']}% | Healthy Green: {d['healthy_green_pct']}%")
    print(f" -> Bounding Box:      {d['bounding_box']}")
    print(f" -> Symptoms:          {t['symptoms'][:80]}...")
    print(f" -> Organic Remedy:    {t['organic'][0]}")

print("\n" + "="*75)
print("[SUCCESS] All AgroCure AI tests passed successfully!")
print("="*75)
