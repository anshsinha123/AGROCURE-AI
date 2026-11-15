import os
from pathlib import Path

base_admin = Path(__file__).resolve().parent / "admin"
dirs = [
    base_admin / "frontend" / "src" / "components",
    base_admin / "frontend" / "src" / "pages",
    base_admin / "frontend" / "src" / "services",
    base_admin / "frontend" / "src" / "context",
    base_admin / "backend" / "controllers",
    base_admin / "backend" / "routes",
    base_admin / "backend" / "middleware",
    base_admin / "backend" / "models",
    base_admin / "backend" / "services",
    base_admin / "backend" / "utils"
]

for d in dirs:
    d.mkdir(parents=True, exist_ok=True)

# 1. adminApi.js
api_service = """/**
 * AgroCure AI - Admin API Service
 * Centralized client for communicating with /api/admin endpoints
 */
const BASE_URL = '/api/admin';

export const adminApi = {
  // Auth
  login: async (email, password) => {
    const res = await fetch(`${BASE_URL}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
    return res.json();
  },
  getProfile: async (token) => {
    const res = await fetch(`${BASE_URL}/auth/profile`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    return res.json();
  },
  logout: async (token) => {
    const res = await fetch(`${BASE_URL}/auth/logout`, {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${token}` }
    });
    return res.json();
  },

  // Dashboard
  getStats: async (token) => {
    const res = await fetch(`${BASE_URL}/dashboard/stats`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    return res.json();
  },
  getAnalytics: async (token) => {
    const res = await fetch(`${BASE_URL}/dashboard/analytics`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    return res.json();
  },

  // Users
  getUsers: async (token, params = {}) => {
    const query = new URLSearchParams(params).toString();
    const res = await fetch(`${BASE_URL}/users?${query}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    return res.json();
  },
  updateUserStatus: async (token, userId, status) => {
    const res = await fetch(`${BASE_URL}/users/${userId}/status`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify({ status })
    });
    return res.json();
  },
  deleteUser: async (token, userId) => {
    const res = await fetch(`${BASE_URL}/users/${userId}`, {
      method: 'DELETE',
      headers: { 'Authorization': `Bearer ${token}` }
    });
    return res.json();
  },

  // Predictions
  getPredictions: async (token, params = {}) => {
    const query = new URLSearchParams(params).toString();
    const res = await fetch(`${BASE_URL}/predictions?${query}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    return res.json();
  },

  // Diseases
  getDiseases: async (token) => {
    const res = await fetch(`${BASE_URL}/diseases`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    return res.json();
  },
  saveDisease: async (token, disease) => {
    const method = disease.id ? 'PUT' : 'POST';
    const url = disease.id ? `${BASE_URL}/diseases/${disease.id}` : `${BASE_URL}/diseases`;
    const res = await fetch(url, {
      method,
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify(disease)
    });
    return res.json();
  },
  deleteDisease: async (token, id) => {
    const res = await fetch(`${BASE_URL}/diseases/${id}`, {
      method: 'DELETE',
      headers: { 'Authorization': `Bearer ${token}` }
    });
    return res.json();
  },

  // Treatments
  getTreatments: async (token) => {
    const res = await fetch(`${BASE_URL}/treatments`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    return res.json();
  },
  saveTreatment: async (token, treatment, isOrganic = true) => {
    const res = await fetch(`${BASE_URL}/treatments?type=${isOrganic ? 'organic' : 'inorganic'}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify(treatment)
    });
    return res.json();
  },

  // Models
  getModels: async (token) => {
    const res = await fetch(`${BASE_URL}/models`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    return res.json();
  },
  activateModel: async (token, id) => {
    const res = await fetch(`${BASE_URL}/models/${id}/activate`, {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${token}` }
    });
    return res.json();
  },

  // Feedback
  getFeedback: async (token) => {
    const res = await fetch(`${BASE_URL}/feedback`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    return res.json();
  },
  updateFeedbackStatus: async (token, id, status, reply = '') => {
    const res = await fetch(`${BASE_URL}/feedback/${id}/status`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify({ status, reply })
    });
    return res.json();
  },

  // Notifications
  getNotifications: async (token) => {
    const res = await fetch(`${BASE_URL}/notifications`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    return res.json();
  },
  createNotification: async (token, notif) => {
    const res = await fetch(`${BASE_URL}/notifications`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify(notif)
    });
    return res.json();
  },

  // Settings
  getSettings: async (token) => {
    const res = await fetch(`${BASE_URL}/settings`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    return res.json();
  },
  updateSettings: async (token, settings) => {
    const res = await fetch(`${BASE_URL}/settings`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify(settings)
    });
    return res.json();
  },

  // Activity Logs
  getActivityLogs: async (token) => {
    const res = await fetch(`${BASE_URL}/activity-logs`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    return res.json();
  }
};
"""
with open(base_admin / "frontend" / "src" / "services" / "adminApi.js", "w", encoding="utf-8") as f:
    f.write(api_service)

# 2. AdminAuthContext.jsx
auth_context = """import React, { createContext, useContext, useState, useEffect } from 'react';
import { adminApi } from '../services/adminApi';

const AdminAuthContext = createContext(null);

export const AdminAuthProvider = ({ children }) => {
  const [adminUser, setAdminUser] = useState(() => {
    const saved = localStorage.getItem('agrocure_admin_user');
    return saved ? JSON.parse(saved) : null;
  });
  const [adminToken, setAdminToken] = useState(() => {
    return localStorage.getItem('agrocure_admin_token') || null;
  });
  const [loading, setLoading] = useState(false);

  const login = async (email, password) => {
    setLoading(true);
    try {
      const data = await adminApi.login(email, password);
      if (data.token && data.admin) {
        setAdminToken(data.token);
        setAdminUser(data.admin);
        localStorage.setItem('agrocure_admin_token', data.token);
        localStorage.setItem('agrocure_admin_user', JSON.stringify(data.admin));
        return { success: true };
      }
      return { success: false, message: data.detail || 'Login failed' };
    } catch (e) {
      return { success: false, message: e.message };
    } finally {
      setLoading(false);
    }
  };

  const logout = () => {
    if (adminToken) adminApi.logout(adminToken).catch(console.warn);
    setAdminUser(null);
    setAdminToken(null);
    localStorage.removeItem('agrocure_admin_user');
    localStorage.removeItem('agrocure_admin_token');
  };

  return (
    <AdminAuthContext.Provider value={{ adminUser, adminToken, login, logout, loading, isAuthenticated: !!adminUser }}>
      {children}
    </AdminAuthContext.Provider>
  );
};

export const useAdminAuth = () => useContext(AdminAuthContext);
"""
with open(base_admin / "frontend" / "src" / "context" / "AdminAuthContext.jsx", "w", encoding="utf-8") as f:
    f.write(auth_context)

# 3. Backend auth middleware
auth_middleware = """/**
 * AgroCure AI - Admin RBAC Middleware
 * Verifies JWT signature and extracts role ('Super Admin', 'Admin', 'Content Manager')
 */
const jwt = require('jsonwebtoken');
const crypto = require('crypto');

const configuredSecret = process.env.AGROCURE_ADMIN_SECRET;
const JWT_SECRET = configuredSecret || crypto.randomBytes(32).toString('hex');

if (!configuredSecret) {
  console.warn('[AgroCure AI] AGROCURE_ADMIN_SECRET is unset; admin tokens will expire after a server restart.');
}

const verifyAdminToken = (req, res, next) => {
  const authHeader = req.headers.authorization;
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ detail: 'Access denied: No authentication token provided.' });
  }

  const token = authHeader.split(' ')[1];
  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    if (!['Super Admin', 'Admin', 'Content Manager'].includes(decoded.role)) {
      return res.status(403).json({ detail: 'Forbidden: Insufficient administrative privileges.' });
    }
    req.admin = decoded;
    next();
  } catch (err) {
    return res.status(401).json({ detail: 'Session expired or invalid token.' });
  }
};

const requireSuperAdmin = (req, res, next) => {
  if (req.admin && req.admin.role === 'Super Admin') {
    return next();
  }
  return res.status(403).json({ detail: 'Forbidden: Action requires Super Admin authority.' });
};

module.exports = { verifyAdminToken, requireSuperAdmin };
"""
with open(base_admin / "backend" / "middleware" / "auth.js", "w", encoding="utf-8") as f:
    f.write(auth_middleware)

print("Modular Admin Panel files generated in admin/ directory.")
