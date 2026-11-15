const mongoose = require('mongoose');

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
