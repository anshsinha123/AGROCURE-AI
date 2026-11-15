const mongoose = require('mongoose');

const ScanSchema = new mongoose.Schema({
  crop: {
    type: String,
    required: true,
    enum: ['Pepper', 'Grapes', 'Wheat', 'Corn']
  },
  disease: {
    type: String,
    required: true
  },
  severity: {
    type: String,
    enum: ['Healthy', 'Low', 'Moderate', 'High', 'Severe']
  },
  confidence: {
    type: Number,
    required: true
  },
  isHealthy: {
    type: Boolean,
    default: false
  },
  leafMetrics: {
    isLeafDetected: Boolean,
    boundingBox: [Number],
    leafCoveragePct: Number,
    healthyGreenPct: Number,
    lesionPct: Number
  },
  treatment: {
    symptoms: String,
    organic: [String],
    chemical: [String],
    prevention: [String]
  },
  language: {
    type: String,
    default: 'en',
    enum: ['en', 'hi', 'kn']
  },
  imageUrl: String,
  createdAt: {
    type: Date,
    default: Date.now
  }
});

module.exports = mongoose.model('Scan', ScanSchema);
