# AgroCure AI – AI-Powered Agricultural Assistant for Inclusive Plant Disease Detection

An intelligent, full-stack agricultural web platform engineered to detect foliar crop diseases, segment necrotic lesions, and deliver actionable organic and chemical treatments. Built with deep linguistic inclusivity for Indian farmers, offering real-time translations and voice assistance in **English**, **Hindi (हिंदी)**, and **Kannada (ಕನ್ನಡ)**.

---

## 🌾 Supported Crops & Pathologies

| Crop | Scientific Name | Target Pathologies & Conditions |
| :--- | :--- | :--- |
| **Pepper (Capsicum)** | *Capsicum annuum* | Bacterial Spot (*Xanthomonas euvesicatoria*), Healthy Leaf |
| **Grapes** | *Vitis vinifera* | Black Rot (*Guignardia bidwellii*), Esca / Black Measles (*Phaeomoniella*), Healthy Leaf |
| **Wheat** | *Triticum aestivum* | Yellow / Stripe Rust (*Puccinia striiformis*), Brown / Leaf Rust (*Puccinia triticina*), Powdery Mildew (*Blumeria graminis*), Healthy Plant |
| **Corn (Maize)** | *Zea mays* | Common Rust (*Puccinia sorghi*), Gray Leaf Spot (*Cercospora zeae-maydis*), Northern Corn Leaf Blight (*Exserohilum turcicum*), Healthy Leaf |

---

## 🤖 Integrated Machine Learning Models

AgroCure AI supports multi-model inference with side-by-side comparative consensus:

| Model | Checkpoint Origin | Architecture | Supported Classes | Supported Crops |
| :--- | :--- | :--- | :--- | :--- |
| **Model 1 (Primary)** | `ai_engine/inference.py` | MobileNetV2 + OpenCV Foliar Telemetry | **19 Classes** | Tomato, Potato, Capsicum, Grapes |
| **Model 2 (Colab)** | `models/final_plant_disease_model.keras` | Deep CNN with 15-Class Dense Head `(1280, 15)` | **15 Classes** | Tomato, Potato, Capsicum |
| **Dual Comparison** | `ai_engine/multi_model_service.py` | Concurrent Parallel Execution & Consensus | **Consensus Evaluation** | Tomato, Potato, Capsicum, Grapes |

---

## 🛠️ Technology Stack

- **Frontend**: **React.js 18**, Tailwind CSS, FontAwesome 6, Web Speech Synthesis API (Audio Voice Guidance in EN/HI/KN).
- **Backend**: **Node.js** & **Express.js** REST API with Multer file uploads, and a high-performance **FastAPI** gateway.
- **Deep Learning Model**: **TensorFlow / Keras** & **PyTorch** **MobileNetV2** (Inverted Residual Depthwise Separable Convolutions).
- **Computer Vision**: **OpenCV** & **NumPy** vegetative indices (**Excess Green Index - ExG**, **Green Leaf Index - GLI**, dynamic bounding box `[ymin, xmin, ymax, xmax]`, and lesion heatmaps).
- **Database**: **MongoDB** with Mongoose schema (`ScanSchema`) and persistent local JSON fallback (`scans_history.json`).
- **Languages**: **English (en)**, **Hindi (hi - हिंदी)**, **Kannada (kn - ಕನ್ನಡ)**.

---

## 🚀 Quick Start Guide

### 1. Launch the AgroCure AI Platform
Install the Python dependencies, then ensure MongoDB is running locally at
`mongodb://127.0.0.1:27017/agrocure_ai` (or set `MONGODB_URI` to another connection string):
```powershell
cd C:\path\to\agrocure_ai
python -m pip install -r requirements.txt
python -m uvicorn backend.app_server:app --host 127.0.0.1 --port 5000 --reload
```
The requirements install the TensorFlow runtime needed to load the complete
Google Colab Model 2 checkpoint. Restart the server after installing dependencies.
Do not commit a URI containing database credentials. `MONGODB_DB_NAME` optionally
overrides the database name in the URI; otherwise the app uses the URI's database
or `agrocure_ai`.
*(Or double-click [run_agrocure.bat](./run_agrocure.bat))*

Open your browser at: **`http://127.0.0.1:5000`**

### Streamlit Community Cloud
The repository also includes a Streamlit app for the Model 2 image-diagnosis
workflow. It supports tomato, potato, and capsicum; the existing React/FastAPI
site, login, admin portal, and MongoDB-backed features remain available through
the regular application and are not part of this Streamlit entry point.

Run it locally from the project root:
```powershell
streamlit run streamlit_app.py
```

To deploy, connect the GitHub repository to
[Streamlit Community Cloud](https://share.streamlit.io), choose branch `main`,
and set `streamlit_app.py` as the app file. The app uses the repository's
`requirements.txt` and needs no database secrets. Keep Python on a version
supported by TensorFlow (Python 3.12 is the configured Cloud default).

### Administrator Setup
No demo user or administrator accounts are created. To create an initial admin,
set `AGROCURE_INITIAL_ADMIN_EMAIL` and `AGROCURE_INITIAL_ADMIN_PASSWORD` in the
environment, then run `python init_admin_data.py`. The script creates the admin
using those values and seeds the catalog data.

Set `AGROCURE_ADMIN_AUTH_SECRET` for persistent FastAPI admin sessions and
`AGROCURE_ADMIN_SECRET` for the separate Node.js admin API. If unset, each
process uses a random temporary key, so tokens become invalid after a restart.
Keep these values in your deployment environment and never commit them.

The FastAPI server stores users, scans, feedback, messages, and team data in the
`agrocure_ai` MongoDB database when connected. On first connection it imports
existing JSON data into empty collections. If MongoDB is unavailable, the app logs the connection
failure and continues using its JSON files; `/api/status` reports the active
storage backend.

### Managing Development Team Profiles
Sign in with an Admin or Developer account, open **About Us**, and select
**Edit Profile** on a team member card. You can update profile details, skills,
links, and photo; changes are saved through the role-protected API to MongoDB
(or the JSON fallback). Team edit sessions use signed bearer tokens that expire
after 24 hours. Set `AGROCURE_AUTH_SECRET` to a stable private value if tokens
should remain valid across server restarts.

### 2. Node.js & Express / MongoDB Execution (Alternative)
```powershell
cd C:\path\to\agrocure_ai\backend
npm install
node server.js
```

---

## 📂 Project Architecture

```
agrocure_ai/
├── models/
│   ├── final_plant_disease_model.keras   # Exported Google Colab Model (9.86 MB)
│   └── class_names.json                  # 15 Colab target classes
├── backend/
│   ├── app_server.py           # Unified FastAPI / Uvicorn server (/api/models, /api/scan, /api/scan/compare)
│   ├── admin_routes.py         # Administrator portal endpoints & analytics
│   ├── server.js               # Node.js & Express.js REST API server
│   └── package.json            # Node dependencies (express, mongoose, multer, cors)
├── frontend/
│   ├── index.html              # React.js 14-Page Single-Page Application with Model Selection
│   ├── admin.html              # Admin portal frontend
│   └── translations.js         # Complete UI dictionaries in English, Hindi, Kannada, Tamil, Marathi
├── ai_engine/
│   ├── colab_engine.py         # Model 2 Google Colab inference engine
│   ├── multi_model_service.py  # Multi-model orchestrator & comparative consensus engine
│   ├── inference.py            # Model 1 MobileNetV2 foliar engine (Primary)
│   ├── disease_catalog.py      # Multilingual agricultural pathology & treatment knowledge base
│   └── cv_detector.py          # OpenCV leaf boundary detection & lesion segmentation
├── data/
│   ├── scans_history.json      # Persistent farmer diagnostic scan log with Model tracking
│   └── users.json              # Registered user accounts & roles
├── static/
│   └── samples/                # Preloaded test leaves for instant 1-click evaluation
├── test_multi_model.py         # Multi-model unit verification script
├── test_endpoints.py           # Comprehensive API route tester
└── run_agrocure.bat            # 1-Click launcher
```
