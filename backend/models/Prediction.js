const mongoose = require('mongoose');

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
