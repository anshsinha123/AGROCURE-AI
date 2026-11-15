const mongoose = require('mongoose');

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
