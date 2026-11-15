const mongoose = require('mongoose');

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
