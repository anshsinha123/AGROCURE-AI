from pathlib import Path

models_dir = Path(__file__).resolve().parent / "backend" / "models"
models_dir.mkdir(parents=True, exist_ok=True)

models = {
    "Admin.js": """const mongoose = require('mongoose');

const AdminSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password_hash: { type: String, required: true },
  role: { type: String, enum: ['Super Admin', 'Admin', 'Content Manager'], default: 'Admin' },
  avatar: { type: String, default: '/static/team/dev1.png' },
  department: { type: String, default: 'Technical Operations' },
  status: { type: String, enum: ['Active', 'Suspended'], default: 'Active' },
  last_login: { type: Date, default: Date.now },
  created_at: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Admin', AdminSchema);
""",

    "User.js": """const mongoose = require('mongoose');

const UserSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password_hash: { type: String, required: true },
  role: { type: String, enum: ['Farmer', 'Agronomist', 'Researcher', 'Student', 'Developer', 'Admin'], default: 'Farmer' },
  farm_location: { type: String, default: 'General Farm' },
  farm_size: { type: String, default: '3 Acres' },
  preferred_crop: { type: String, default: 'Tomato' },
  preferred_lang: { type: String, default: 'en' },
  theme: { type: String, default: 'light' },
  avatar: { type: String, default: null },
  phone: { type: String, default: null },
  bio: { type: String, default: null },
  status: { type: String, enum: ['Active', 'Suspended', 'Pending'], default: 'Active' },
  created_at: { type: Date, default: Date.now }
});

module.exports = mongoose.model('User', UserSchema);
""",

    "Prediction.js": """const mongoose = require('mongoose');

const PredictionSchema = new mongoose.Schema({
  user_id: { type: String, default: 'Guest' },
  user_name: { type: String, default: 'Anonymous' },
  crop: { type: String, enum: ['Tomato', 'Potato', 'Capsicum', 'Grapes'], required: true },
  disease: { type: String, required: true },
  confidence: { type: Number, required: true },
  is_healthy: { type: Boolean, default: false },
  severity: { type: String, enum: ['None', 'Low', 'Moderate', 'High', 'Severe'], default: 'Moderate' },
  image_url: { type: String, required: true },
  annotated_image: { type: String, default: null },
  healthy_green_pct: { type: Number, default: 0 },
  lesion_pct: { type: Number, default: 0 },
  lang: { type: String, default: 'en' },
  created_at: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Prediction', PredictionSchema);
""",

    "Disease.js": """const mongoose = require('mongoose');

const DiseaseSchema = new mongoose.Schema({
  crop: { type: String, enum: ['Tomato', 'Potato', 'Capsicum', 'Grapes'], required: true },
  name: { type: String, required: true, unique: true },
  scientific_name: { type: String, required: true },
  severity: { type: String, required: true },
  status: { type: String, enum: ['Active', 'Draft'], default: 'Active' },
  description: { type: String, required: true },
  symptoms: { type: String, required: true },
  causes: { type: String, required: true },
  prevention: { type: String, required: true },
  image: { type: String, default: '/static/samples/sample_tomato_early_blight.jpg' },
  updated_at: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Disease', DiseaseSchema);
""",

    "OrganicTreatment.js": """const mongoose = require('mongoose');

const OrganicTreatmentSchema = new mongoose.Schema({
  name: { type: String, required: true },
  category: { type: String, required: true },
  assigned_diseases: [{ type: String }],
  instructions: { type: String, required: true },
  frequency: { type: String, required: true },
  precautions: { type: String, required: true },
  image: { type: String, default: null },
  updated_at: { type: Date, default: Date.now }
});

module.exports = mongoose.model('OrganicTreatment', OrganicTreatmentSchema);
""",

    "InorganicTreatment.js": """const mongoose = require('mongoose');

const InorganicTreatmentSchema = new mongoose.Schema({
  product_name: { type: String, required: true },
  active_ingredient: { type: String, required: true },
  cibrc_registration: { type: String, required: true },
  assigned_diseases: [{ type: String }],
  dosage: { type: String, required: true },
  phi_days: { type: Number, default: 7 },
  ppe: { type: String, required: true },
  precautions: { type: String, required: true },
  status: { type: String, enum: ['Approved', 'Under Review', 'Restricted'], default: 'Approved' },
  updated_at: { type: Date, default: Date.now }
});

module.exports = mongoose.model('InorganicTreatment', InorganicTreatmentSchema);
""",

    "Feedback.js": """const mongoose = require('mongoose');

const FeedbackSchema = new mongoose.Schema({
  name: { type: String, required: true },
  role: { type: String, default: 'Farmer' },
  crop: { type: String, default: 'Tomato' },
  rating: { type: Number, min: 1, max: 5, default: 5 },
  comment: { type: String, required: true },
  status: { type: String, enum: ['New', 'Reviewed', 'Resolved'], default: 'New' },
  admin_reply: { type: String, default: null },
  created_at: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Feedback', FeedbackSchema);
""",

    "Notification.js": """const mongoose = require('mongoose');

const NotificationSchema = new mongoose.Schema({
  title: { type: String, required: true },
  type: { type: String, enum: ['Disease Outbreak Alert', 'Maintenance', 'Feature Update', 'General Announcement'], default: 'General Announcement' },
  priority: { type: String, enum: ['Low', 'Medium', 'High', 'Critical'], default: 'Medium' },
  target_audience: { type: String, default: 'All Users' },
  message: { type: String, required: true },
  created_by: { type: String, required: true },
  status: { type: String, enum: ['Draft', 'Scheduled', 'Sent'], default: 'Sent' },
  created_at: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Notification', NotificationSchema);
""",

    "ModelVersion.js": """const mongoose = require('mongoose');

const ModelVersionSchema = new mongoose.Schema({
  name: { type: String, required: true },
  version: { type: String, required: true, unique: true },
  framework: { type: String, default: 'TensorFlow / Keras' },
  training_date: { type: String, required: true },
  classes_count: { type: Number, default: 19 },
  input_shape: [{ type: Number }],
  test_accuracy: { type: Number, required: true },
  test_precision: { type: Number, required: true },
  test_recall: { type: Number, required: true },
  f1_score: { type: Number, required: true },
  avg_latency_ms: { type: Number, default: 45 },
  file_size_mb: { type: Number, default: 14.2 },
  status: { type: String, enum: ['Active', 'Archived', 'Rollback Ready'], default: 'Archived' },
  deployed_at: { type: Date, default: Date.now }
});

module.exports = mongoose.model('ModelVersion', ModelVersionSchema);
""",

    "AdminActivityLog.js": """const mongoose = require('mongoose');

const AdminActivityLogSchema = new mongoose.Schema({
  admin_id: { type: String, required: true },
  admin_name: { type: String, required: true },
  role: { type: String, required: true },
  action: { type: String, required: true },
  description: { type: String, required: true },
  target_id: { type: String, default: null },
  ip_address: { type: String, default: '127.0.0.1' },
  timestamp: { type: Date, default: Date.now }
});

module.exports = mongoose.model('AdminActivityLog', AdminActivityLogSchema);
""",

    "SystemSettings.js": """const mongoose = require('mongoose');

const SystemSettingsSchema = new mongoose.Schema({
  site_name: { type: String, default: 'AGROCURE AI' },
  site_tagline: { type: String, default: 'AI-Based Plant Disease Detection System' },
  logo_url: { type: String, default: '/static/team/dev1.png' },
  confidence_threshold: { type: Number, default: 75.0 },
  max_upload_size_mb: { type: Number, default: 15 },
  maintenance_mode: { type: Boolean, default: false },
  contact_email: { type: String, default: 'support@agrocure.ai' },
  supported_crops: [{ type: String }],
  supported_languages: [{ type: String }],
  updated_at: { type: Date, default: Date.now }
});

module.exports = mongoose.model('SystemSettings', SystemSettingsSchema);
"""
}

for fname, code in models.items():
    with open(models_dir / fname, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Created model: {fname}")

print("All 11 Mongoose models created successfully.")
