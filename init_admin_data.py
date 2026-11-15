import json
import hashlib
import os
from pathlib import Path
from datetime import datetime

data_dir = Path(__file__).resolve().parent / "data"
data_dir.mkdir(parents=True, exist_ok=True)

def hash_pw(pw: str) -> str:
    # Use sha256 with consistent salt for college project simplicity
    salt = "agrocure_salt_2026"
    return hashlib.sha256((pw + salt).encode()).hexdigest()

# 1. ADMINS
admin_email = os.getenv("AGROCURE_INITIAL_ADMIN_EMAIL")
admin_password = os.getenv("AGROCURE_INITIAL_ADMIN_PASSWORD")
if bool(admin_email) != bool(admin_password):
    raise SystemExit("Set both AGROCURE_INITIAL_ADMIN_EMAIL and AGROCURE_INITIAL_ADMIN_PASSWORD to seed an admin.")

admins = []
if admin_email and admin_password:
    admins.append({
        "id": "adm_initial_01",
        "name": os.getenv("AGROCURE_INITIAL_ADMIN_NAME", "AgroCure Administrator"),
        "email": admin_email.strip().lower(),
        "password_hash": hash_pw(admin_password),
        "role": "Super Admin",
        "avatar": "/static/team/dev1.png",
        "department": "Operations",
        "status": "Active",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "last_login": ""
    })
with open(data_dir / "admins.json", "w", encoding="utf-8") as f:
    json.dump(admins, f, indent=2)

# 2. DISEASES (Comprehensive Catalog across Tomato, Potato, Capsicum, Grapes)
diseases = [
    {
        "id": "dis_tom_01",
        "crop": "Tomato",
        "name": "Tomato Early Blight",
        "scientific_name": "Alternaria solani",
        "severity": "Moderate to High",
        "status": "Active",
        "description": "Fungal disease causing concentric target-board dark rings on older lower leaves, leading to yellowing and premature defoliation.",
        "symptoms": "Concentric rings with chlorotic halo, dark brown to black circular lesions, stems exhibit dark sunken cankers.",
        "causes": "Warm temperatures (24-29°C) combined with high humidity, heavy rain, or overhead sprinkler irrigation.",
        "prevention": "Crop rotation of 2-3 years, mulching soil to prevent spore splash, drip irrigation, resistant varieties.",
        "image": "/static/samples/sample_tomato_early_blight.jpg"
    },
    {
        "id": "dis_tom_02",
        "crop": "Tomato",
        "name": "Tomato Late Blight",
        "scientific_name": "Phytophthora infestans",
        "severity": "Severe / Critical",
        "status": "Active",
        "description": "Rapidly destructive water-mold oomycete causing pale, water-soaked foliage lesions that quickly turn dark brown with white fuzzy fungal growth beneath.",
        "symptoms": "Irregular water-soaked spots, white sporulation on undersides of leaves during humid mornings, stem collapse.",
        "causes": "Cool, wet weather (15-20°C) with prolonged relative humidity exceeding 90%.",
        "prevention": "Destroy cull piles, use certified disease-free transplants, maximize airflow, prophylactic biofungicides.",
        "image": "/static/samples/sample_tomato_early_blight.jpg"
    },
    {
        "id": "dis_tom_03",
        "crop": "Tomato",
        "name": "Tomato Bacterial Spot",
        "scientific_name": "Xanthomonas vesicatoria",
        "severity": "High",
        "status": "Active",
        "description": "Bacterial infection creating tiny water-soaked lesions that turn angular, dark brown, and scabby on leaves and fruits.",
        "symptoms": "Angular dark spots (1-3mm) with yellow halos, shot-hole effect as lesion centers fall out.",
        "causes": "Splashing rain, warm temperatures (25-30°C), contaminated seed stock.",
        "prevention": "Hot water seed treatment, copper-bactericide sprays, avoid working in wet fields.",
        "image": "/static/samples/sample_capsicum_bacterial_spot.jpg"
    },
    {
        "id": "dis_pot_01",
        "crop": "Potato",
        "name": "Potato Late Blight",
        "scientific_name": "Phytophthora infestans",
        "severity": "Severe / Epidemic",
        "status": "Active",
        "description": "The historical pathogen of the Irish Famine; rapidly destroys foliage and infects tubers with dry brown rot.",
        "symptoms": "Dark brown greasy water-soaked lesions expanding rapidly across foliage; white mildew rim under humid mornings.",
        "causes": "Excess canopy moisture, fog, temperatures between 12°C and 22°C.",
        "prevention": "Planting certified seed tubers, early application of copper bio-fungicide, proper hilling.",
        "image": "/static/samples/sample_potato_late_blight.jpg"
    },
    {
        "id": "dis_pot_02",
        "crop": "Potato",
        "name": "Potato Early Blight",
        "scientific_name": "Alternaria solani",
        "severity": "Moderate",
        "status": "Active",
        "description": "Common foliar affliction characterized by target-like concentric rings restricted by leaf veins.",
        "symptoms": "Brown circular spots on lower mature foliage with concentric target rings and yellow margin.",
        "causes": "Foliar stress, alternating wet and dry weather, nutrient deficiency.",
        "prevention": "Adequate nitrogen fertilization, balanced irrigation, removal of volunteer solanaceous weeds.",
        "image": "/static/samples/sample_potato_late_blight.jpg"
    },
    {
        "id": "dis_cap_01",
        "crop": "Capsicum",
        "name": "Capsicum Bacterial Spot",
        "scientific_name": "Xanthomonas campestris pv. vesicatoria",
        "severity": "High",
        "status": "Active",
        "description": "Severe foliar disease in sweet bell peppers causing defoliation and sunscald injury to exposed fruit.",
        "symptoms": "Small, yellow-green circular lesions that darken into water-soaked brown spots with raised pustules.",
        "causes": "High humidity, overhead watering, infected transplants.",
        "prevention": "Disinfection of greenhouse trays, drip irrigation, application of copper hydroxides.",
        "image": "/static/samples/sample_capsicum_bacterial_spot.jpg"
    },
    {
        "id": "dis_grp_01",
        "crop": "Grapes",
        "name": "Grapes Black Rot",
        "scientific_name": "Guignardia bidwellii",
        "severity": "Severe",
        "status": "Active",
        "description": "Fungal infection affecting all green grape tissue; leaves develop reddish-brown circular spots with black pycnidia dots, fruits shrivel into hard black mummies.",
        "symptoms": "Reddish-brown circular necrotic spots with tiny black fruiting bodies; berry mummification.",
        "causes": "Prolonged leaf wetness during bloom and shoot expansion; temperatures 20-27°C.",
        "prevention": "Canopy pruning for optimal sun and wind penetration, mummified cluster destruction.",
        "image": "/static/samples/sample_grapes_black_rot.jpg"
    },
    {
        "id": "dis_grp_02",
        "crop": "Grapes",
        "name": "Grapes Esca (Black Measles)",
        "scientific_name": "Phaeomoniella chlamydospora & Fomitiporia",
        "severity": "High / Vascular",
        "status": "Active",
        "description": "Complex trunk disease causing tiger-stripe interveinal leaf chlorosis and dark speckling on berries.",
        "symptoms": "Tiger-stripe yellow/brown bands between green leaf veins; sudden vine apoplexy wilt in midsummer.",
        "causes": "Pruning wound infections by fungal spores during rainy dormant periods.",
        "prevention": "Pruning wound sealants, Trichoderma biocontrol application to cane cuts, delayed winter pruning.",
        "image": "/static/samples/sample_grapes_black_rot.jpg"
    }
]
with open(data_dir / "diseases.json", "w", encoding="utf-8") as f:
    json.dump(diseases, f, indent=2)

# 3. ORGANIC TREATMENTS
organic_treatments = [
    {
        "id": "org_01",
        "name": "Cold-Pressed Neem Oil (Azadirachtin 10,000 PPM)",
        "category": "Botanical Bio-fungicide & Repellent",
        "assigned_diseases": ["Tomato Early Blight", "Tomato Bacterial Spot", "Capsicum Bacterial Spot"],
        "instructions": "Mix 5ml pure neem oil + 2ml organic liquid soap per 1 liter of soft water. Agitate vigorously until milky emulsion forms. Spray foliar undersides thoroughly at dusk.",
        "frequency": "Every 7 to 10 days prophylactically, or every 5 days during active foliar symptoms.",
        "precautions": "Avoid application during peak midday sunlight (>32°C) to prevent foliar phytotoxicity scorch. Test on small patch 24h prior.",
        "image": "/static/samples/sample_tomato_early_blight.jpg"
    },
    {
        "id": "org_02",
        "name": "Trichoderma viride / harzianum Bio-Inoculant",
        "category": "Beneficial Antagonistic Microbe",
        "assigned_diseases": ["Tomato Late Blight", "Potato Late Blight", "Grapes Black Rot"],
        "instructions": "Dissolve 50g Trichoderma wettable powder (2x10^6 CFU/g) in 10 liters clean non-chlorinated water. Apply as foliar drench and root zone soak to outcompete soilborne oomycetes.",
        "frequency": "At transplanting, then every 14 days during vegetative flushes.",
        "precautions": "Do not mix with synthetic copper fungicides or antibiotics within 7 days, as copper degrades viable fungal spores.",
        "image": "/static/samples/sample_potato_late_blight.jpg"
    },
    {
        "id": "org_03",
        "name": "Pseudomonas fluorescens (Bio-Bactericide)",
        "category": "Bacterial Antagonist & Systemic Inducer",
        "assigned_diseases": ["Tomato Bacterial Spot", "Capsicum Bacterial Spot"],
        "instructions": "Mix 10g per liter of water. Spray canopy thoroughly during early morning dew to induce systemic acquired resistance (SAR).",
        "frequency": "Bi-weekly throughout nursery and early flowering.",
        "precautions": "Store microbial packets in cool shade below 25°C. Check expiration date for high viable colony counts.",
        "image": "/static/samples/sample_capsicum_bacterial_spot.jpg"
    },
    {
        "id": "org_04",
        "name": "Potassium Bicarbonate Eco-Fungicide",
        "category": "Natural Mineral Contact Fungicide",
        "assigned_diseases": ["Grapes Black Rot", "Tomato Early Blight", "Potato Early Blight"],
        "instructions": "Dissolve 4g potassium bicarbonate + 2ml horticultural oil per liter water. Disrupts fungal cell wall osmotic pressure on contact.",
        "frequency": "Spray immediately upon first lesion detection, repeat after heavy rainfall.",
        "precautions": "Ensure spray solution pH remains near 8.0-8.5. Do not overdose on tender young grape shoots.",
        "image": "/static/samples/sample_grapes_black_rot.jpg"
    }
]
with open(data_dir / "organic_treatments.json", "w", encoding="utf-8") as f:
    json.dump(organic_treatments, f, indent=2)

# 4. INORGANIC TREATMENTS (Verified Product Label Guidelines)
inorganic_treatments = [
    {
        "id": "chem_01",
        "product_name": "Mancozeb 75% WP (Dithane M-45)",
        "active_ingredient": "Mancozeb (Ethylene bisdithiocarbamate) 75% w/w",
        "cibrc_registration": "CIR-14,208/91-Mancozeb(WP)-112",
        "assigned_diseases": ["Tomato Early Blight", "Potato Late Blight", "Grapes Black Rot"],
        "dosage": "2.0 to 2.5 grams per 1 liter water (600-800g per acre)",
        "phi_days": 7,
        "ppe": "Chemical-resistant nitrile gloves, N95 respiratory mask, full sleeve coveralls, protective eye goggles.",
        "precautions": "Broad-spectrum contact protective fungicide. Must be applied prior to spore germination. Do not exceed 4 consecutive sprays to mitigate soil manganese accumulation.",
        "status": "Approved"
    },
    {
        "id": "chem_02",
        "product_name": "Metalaxyl 8% + Mancozeb 64% WP (Ridomil Gold)",
        "active_ingredient": "Metalaxyl-M 8% + Mancozeb 64% w/w",
        "cibrc_registration": "CIR-22,410/96-Metalaxyl+Mancozeb-402",
        "assigned_diseases": ["Tomato Late Blight", "Potato Late Blight"],
        "dosage": "1.5 to 2.0 grams per 1 liter water (500g per acre)",
        "phi_days": 10,
        "ppe": "Nitrile rubber gloves, chemical splash goggles, vapor respirator, rubber boots.",
        "precautions": "Systemic and contact action. Highly effective for emergency blight arrest. Never use more than two consecutive applications per season to prevent phenylamide fungal resistance.",
        "status": "Approved"
    },
    {
        "id": "chem_03",
        "product_name": "Copper Oxychloride 50% WP (Blitox 50)",
        "active_ingredient": "Copper Oxychloride 50% metallic copper equivalent",
        "cibrc_registration": "CIR-8,912/88-Copper(WP)-89",
        "assigned_diseases": ["Tomato Bacterial Spot", "Capsicum Bacterial Spot", "Grapes Black Rot"],
        "dosage": "2.5 to 3.0 grams per 1 liter water (1 kg per acre)",
        "phi_days": 5,
        "ppe": "Face shield, rubber apron, heavy-duty gloves, particulate respirator.",
        "precautions": "Broad spectrum protective bactericide and fungicide. Avoid spraying on flowers or under hot sun to prevent russeting. Maintain neutral spray tank pH.",
        "status": "Approved"
    },
    {
        "id": "chem_04",
        "product_name": "Azoxystrobin 23% SC (Amistar)",
        "active_ingredient": "Azoxystrobin (Strobilurin) 23% w/w",
        "cibrc_registration": "CIR-35,119/2001-Azoxystrobin(SC)-210",
        "assigned_diseases": ["Tomato Early Blight", "Grapes Black Rot"],
        "dosage": "1.0 ml per 1 liter water (200 ml per acre)",
        "phi_days": 5,
        "ppe": "Protective eyewear, chemical-resistant gloves, organic vapor respirator.",
        "precautions": "Inhibits mitochondrial respiration. Rotate with different chemical modes of action (FRAC Group 11) to prevent fungal strain tolerance.",
        "status": "Approved"
    }
]
with open(data_dir / "inorganic_treatments.json", "w", encoding="utf-8") as f:
    json.dump(inorganic_treatments, f, indent=2)

# 5. MULTILINGUAL CONTENT (7 Languages: en, hi, bn, pa, mr, ta, te)
multilingual_content = {
    "supported_languages": [
        {"code": "en", "name": "English", "native": "English", "status": "Published"},
        {"code": "hi", "name": "Hindi", "native": "हिन्दी", "status": "Published"},
        {"code": "bn", "name": "Bengali", "native": "বাংলা", "status": "Published"},
        {"code": "pa", "name": "Punjabi", "native": "ਪੰਜਾਬੀ", "status": "Published"},
        {"code": "mr", "name": "Marathi", "native": "मराठी", "status": "Published"},
        {"code": "ta", "name": "Tamil", "native": "தமிழ்", "status": "Published"},
        {"code": "te", "name": "Telugu", "native": "తెలుగు", "status": "Published"}
    ],
    "translations": {
        "dashboard_title": {
            "en": "AI Plant Pathology Dashboard",
            "hi": "एआई पौध रोग निदान डैशबोर्ड",
            "bn": "এআই উদ্ভিদ রোগ নির্ণয় ড্যাশবোর্ড",
            "pa": "ਏਆਈ ਪੌਦਾ ਰੋਗ ਜਾਂਚ ਡੈਸ਼ਬੋਰਡ",
            "mr": "एआय वनस्पती रोग निदान डॅशबोर्ड",
            "ta": "AI தாவர நோய் கண்டறிதல் டாஷ்போர்டு",
            "te": "AI మొక్కల వ్యాధి నిర్ధారణ డాష్‌బోర్డ్"
        },
        "scan_now": {
            "en": "Scan Leaf Now",
            "hi": "पत्ती की जांच करें",
            "bn": "পাতা স্ক্যান করুন",
            "pa": "ਪੱਤਾ ਸਕੈਨ ਕਰੋ",
            "mr": "पानाचे स्कॅन करा",
            "ta": "இலையை ஸ்கேன் செய்க",
            "te": "ఆకును స్కాన్ చేయండి"
        },
        "healthy_leaf": {
            "en": "Healthy Foliage",
            "hi": "स्वस्थ पत्ता",
            "bn": "সুস্থ পাতা",
            "pa": "ਸਿਹਤਮੰਦ ਪੱਤਾ",
            "mr": "निरोगी पान",
            "ta": "ஆரோக்கியமான இலை",
            "te": "ఆరోగ్యకరమైన ఆకు"
        }
    }
}
with open(data_dir / "multilingual.json", "w", encoding="utf-8") as f:
    json.dump(multilingual_content, f, indent=2, ensure_ascii=False)

# 6. ML MODEL VERSIONS
model_versions = [
    {
        "id": "mdl_v241",
        "name": "MobileNetV2 Foliar Checkpoint v2.4.1",
        "version": "2.4.1",
        "framework": "TensorFlow 2.15 / Keras CNN",
        "training_date": "2026-10-25",
        "classes_count": 19,
        "input_shape": [224, 224, 3],
        "test_accuracy": 98.4,
        "test_precision": 97.8,
        "test_recall": 98.1,
        "f1_score": 97.9,
        "avg_latency_ms": 42.5,
        "file_size_mb": 14.2,
        "status": "Active",
        "deployed_at": "2026-11-01 10:00:00",
        "error_rate": 1.6
    },
    {
        "id": "mdl_v230",
        "name": "MobileNetV2 Foliar Checkpoint v2.3.0",
        "version": "2.3.0",
        "framework": "TensorFlow 2.14 / Keras",
        "training_date": "2026-08-15",
        "classes_count": 19,
        "input_shape": [224, 224, 3],
        "test_accuracy": 96.8,
        "test_precision": 96.1,
        "test_recall": 96.5,
        "f1_score": 96.3,
        "avg_latency_ms": 48.0,
        "file_size_mb": 14.1,
        "status": "Archived",
        "deployed_at": "2026-08-20 14:00:00",
        "error_rate": 3.2
    },
    {
        "id": "mdl_v220",
        "name": "Custom 6-Layer CNN Baseline v2.2.0",
        "version": "2.2.0",
        "framework": "Keras Sequential",
        "training_date": "2026-06-10",
        "classes_count": 19,
        "input_shape": [224, 224, 3],
        "test_accuracy": 94.2,
        "test_precision": 93.5,
        "test_recall": 93.8,
        "f1_score": 93.6,
        "avg_latency_ms": 65.0,
        "file_size_mb": 38.6,
        "status": "Rollback Ready",
        "deployed_at": "2026-06-15 09:00:00",
        "error_rate": 5.8
    }
]
with open(data_dir / "model_versions.json", "w", encoding="utf-8") as f:
    json.dump(model_versions, f, indent=2)

# 7. NOTIFICATIONS & ANNOUNCEMENTS
notifications = [
    {
        "id": "notif_01",
        "title": "Severe Early Blight Alert in Maharashtra & Karnataka",
        "type": "Disease Outbreak Alert",
        "priority": "High",
        "target_audience": "Tomato & Potato Farmers",
        "message": "Continuous rainfall and high humidity (90%+) have triggered regional Alternaria solani spore dispersion. Prophylactic application of bio-neem oil or Mancozeb 75% WP is advised.",
        "created_by": "Dr. Rajeshwar Rao (Super Admin)",
        "created_at": "2026-11-13 08:30:00",
        "status": "Sent"
    },
    {
        "id": "notif_02",
        "title": "Scheduled Server Optimization & Model Checkpoint v2.4",
        "type": "Maintenance",
        "priority": "Medium",
        "target_audience": "All Users",
        "message": "AgroCure AI neural engine will undergo automated tensor optimization on Sunday between 02:00 AM and 03:00 AM IST. Leaf diagnostics will remain accessible without downtime.",
        "created_by": "Abhishek Singh Patel (Admin)",
        "created_at": "2026-11-12 16:00:00",
        "status": "Scheduled"
    },
    {
        "id": "notif_03",
        "title": "New Multilingual Voice Advisory in Bengali & Punjabi",
        "type": "Feature Update",
        "priority": "Low",
        "target_audience": "All Users",
        "message": "We have expanded our vernacular audio advisory support to 7 regional languages! Experience native speech diagnosis on all foliar scan results.",
        "created_by": "Priya Patel (Content Manager)",
        "created_at": "2026-11-11 11:15:00",
        "status": "Sent"
    }
]
with open(data_dir / "notifications.json", "w", encoding="utf-8") as f:
    json.dump(notifications, f, indent=2)

# 8. ACTIVITY LOGS (Immutable Audit Trail)
activity_logs = [
    {
        "id": "log_101",
        "admin_id": "adm_super_01",
        "admin_name": "Dr. Rajeshwar Rao",
        "role": "Super Admin",
        "action": "Admin Login",
        "description": "Authenticated successfully from secure terminal (IP: 127.0.0.1).",
        "target_id": "adm_super_01",
        "timestamp": "2026-11-14 09:30:15"
    },
    {
        "id": "log_102",
        "admin_id": "adm_general_01",
        "admin_name": "Abhishek Singh Patel",
        "role": "Admin",
        "action": "Model Activation",
        "description": "Activated verified neural checkpoint MobileNetV2 v2.4.1 (Test Accuracy: 98.4%).",
        "target_id": "mdl_v241",
        "timestamp": "2026-11-14 10:15:40"
    },
    {
        "id": "log_103",
        "admin_id": "adm_content_01",
        "admin_name": "Priya Patel",
        "role": "Content Manager",
        "action": "Disease Information Update",
        "description": "Updated symptoms and organic prevention guidelines for Capsicum Bacterial Spot.",
        "target_id": "dis_cap_01",
        "timestamp": "2026-11-14 11:20:00"
    },
    {
        "id": "log_104",
        "admin_id": "adm_general_01",
        "admin_name": "Abhishek Singh Patel",
        "role": "Admin",
        "action": "User Status Change",
        "description": "Verified and activated grower account 'Ramesh Patil' (Nashik).",
        "target_id": "usr_farmer_01",
        "timestamp": "2026-11-14 11:35:10"
    }
]
with open(data_dir / "activity_logs.json", "w", encoding="utf-8") as f:
    json.dump(activity_logs, f, indent=2)

# 9. SYSTEM SETTINGS
settings = {
    "site_name": "AGROCURE AI",
    "site_tagline": "AI-Based Plant Disease Detection System for Tomato, Potato, Capsicum, and Grapes",
    "logo_url": "/static/team/dev1.png",
    "confidence_threshold": 75.0,
    "max_upload_size_mb": 15,
    "maintenance_mode": False,
    "contact_email": "support@agrocure.ai",
    "supported_crops": ["Tomato", "Potato", "Capsicum", "Grapes"],
    "supported_languages": ["en", "hi", "bn", "pa", "mr", "ta", "te"],
    "api_version": "2.4.1",
    "service_health": {
        "api_gateway": "Healthy (200 OK)",
        "database": "MongoDB / File Store Synced",
        "ai_inference_engine": "MobileNetV2 Online",
        "file_storage": "Operational"
    }
}
with open(data_dir / "settings.json", "w", encoding="utf-8") as f:
    json.dump(settings, f, indent=2)

print("All 9 admin data collections initialized successfully in data/.")
