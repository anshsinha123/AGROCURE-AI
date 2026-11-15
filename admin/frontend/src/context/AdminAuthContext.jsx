import React, { createContext, useContext, useState, useEffect } from 'react';
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
