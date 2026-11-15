const mongoose = require('mongoose');

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
