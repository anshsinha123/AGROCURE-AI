import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from backend.app_server import get_available_models, scan_sample, get_scans

print("--- Test 1: GET /api/models ---")
models_resp = get_available_models()
data = json.loads(models_resp.body.decode("utf-8"))
print("Status:", data.get("status"))
print("Total Models:", data.get("total_models"))
for m in data.get("models", []):
    print(" - Model:", m["id"], "->", m["name"], f"({m['classes_count']} classes)")

print("\n--- Test 2: POST /api/scan-sample with Model 1 ---")
resp1 = scan_sample("tomato_early_blight", selected_model="model_1")
d1 = json.loads(resp1.body.decode("utf-8")) if hasattr(resp1, "body") else resp1
print("Selected Model:", d1["selected_model"]["name"])
print("Crop:", d1["prediction"]["crop"])
print("Disease:", d1["prediction"]["disease"])
print("Confidence:", str(d1["prediction"]["confidence"]) + "%")
print("Organic Solution Items:", len(d1["treatment"]["organic"]))
print("Chemical Solution Items:", len(d1["treatment"]["chemical"]))

print("\n--- Test 3: POST /api/scan-sample with Model 2 (Colab) ---")
resp2 = scan_sample("tomato_early_blight", selected_model="model_2")
d2 = json.loads(resp2.body.decode("utf-8")) if hasattr(resp2, "body") else resp2
print("Selected Model:", d2["selected_model"]["name"])
print("Crop:", d2["prediction"]["crop"])
print("Disease:", d2["prediction"]["disease"])
print("Confidence:", str(d2["prediction"]["confidence"]) + "%")
print("Organic Solution Items:", len(d2["treatment"]["organic"]))
print("Chemical Solution Items:", len(d2["treatment"]["chemical"]))

print("\n--- Test 4: POST /api/scan-sample with Comparison Mode ---")
resp3 = scan_sample("tomato_early_blight", selected_model="compare")
d3 = json.loads(resp3.body.decode("utf-8")) if hasattr(resp3, "body") else resp3
print("Consensus Status:", d3["comparison"]["status"])
print("Is Agreement:", d3["comparison"]["is_agreement"])
print("Model 1:", d3["comparison"]["model_1_prediction"]["disease"], str(d3["comparison"]["model_1_prediction"]["confidence"]) + "%")
print("Model 2:", d3["comparison"]["model_2_prediction"]["disease"], str(d3["comparison"]["model_2_prediction"]["confidence"]) + "%")
print("Advisory Note:", d3["comparison"]["advisory_note"])

print("\n--- Test 5: GET /api/scans ---")
scans = get_scans()
print("Total Recent Scans:", len(scans))
for s in scans[:3]:
    print("Record:", s["id"], "| Model:", s.get("selected_model"), "| Disease:", s.get("disease"), "| Conf:", str(s.get("confidence")) + "%")

print("\nALL BACKEND API TESTS COMPLETED SUCCESSFULLY!")
