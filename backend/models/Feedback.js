const mongoose = require('mongoose');

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
