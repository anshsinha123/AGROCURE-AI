const mongoose = require('mongoose');

const UserSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password_hash: { type: String, required: true },
  role: { type: String, enum: ['Farmer', 'Agronomist', 'Researcher', 'Student', 'Developer', 'Admin'], default: 'Farmer' },
  farm_location: { type: String, default: 'General Farm' },
  farm_size: { type: String, default: '3 Acres' },
  preferred_crop: { type: String, default: 'Tomato' },
  preferred_lang: { type: String, default: 'en' },
  theme: { type: String, default: 'light' },
  avatar: { type: String, default: null },
  phone: { type: String, default: null },
  bio: { type: String, default: null },
  status: { type: String, enum: ['Active', 'Suspended', 'Pending'], default: 'Active' },
  created_at: { type: Date, default: Date.now }
});

module.exports = mongoose.model('User', UserSchema);
