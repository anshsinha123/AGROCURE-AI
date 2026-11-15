const mongoose = require('mongoose');

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
