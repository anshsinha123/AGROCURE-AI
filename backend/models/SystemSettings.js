const mongoose = require('mongoose');

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
