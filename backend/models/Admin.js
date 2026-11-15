const mongoose = require('mongoose');

const AdminSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password_hash: { type: String, required: true },
  role: { type: String, enum: ['Super Admin', 'Admin', 'Content Manager'], default: 'Admin' },
  avatar: { type: String, default: '/static/team/dev1.png' },
  department: { type: String, default: 'Technical Operations' },
  status: { type: String, enum: ['Active', 'Suspended'], default: 'Active' },
  last_login: { type: Date, default: Date.now },
  created_at: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Admin', AdminSchema);
