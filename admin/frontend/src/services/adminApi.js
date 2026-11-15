/**
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
