const mongoose = require('mongoose');

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
