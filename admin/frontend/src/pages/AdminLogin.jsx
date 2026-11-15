import React, { useState } from 'react';

export const AdminLogin = ({ onLoginSuccess, onReturnToSite }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const res = await fetch('/api/admin/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      });
      const data = await res.json();
      if (res.ok && data.token) {
        onLoginSuccess(data.admin, data.token);
      } else {
        setError(data.detail || 'Invalid administrative credentials.');
      }
    } catch (err) {
      setError(err.message || 'Connection to administrative gateway failed.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 flex items-center justify-center p-4 relative overflow-hidden">
      {/* Background Decorative Rings */}
      <div className="absolute -top-40 -left-40 w-96 h-96 bg-[#14532D]/40 rounded-full blur-3xl pointer-events-none"></div>
      <div className="absolute -bottom-40 -right-40 w-96 h-96 bg-[#22C55E]/20 rounded-full blur-3xl pointer-events-none"></div>

      <div className="w-full max-w-md bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-3xl p-8 shadow-2xl relative z-10 space-y-6">
        {/* Brand Header */}
        <div className="text-center space-y-2">
          <div className="w-14 h-14 mx-auto rounded-2xl bg-[#14532D] text-[#22C55E] flex items-center justify-center text-2xl shadow-lg ring-4 ring-[#22C55E]/30">
            <i className="fa-solid fa-shield-halved"></i>
          </div>
          <h2 className="text-2xl font-black text-slate-900 dark:text-white tracking-tight">AGROCURE AI</h2>
          <span className="inline-block px-3 py-1 rounded-full bg-emerald-100 dark:bg-emerald-950 text-[#14532D] dark:text-emerald-300 text-xs font-mono font-bold uppercase tracking-wider">
            Protected Admin Portal
          </span>
          <p className="text-xs text-slate-500 dark:text-slate-400">
            Authorized access only. All sessions are cryptographically logged.
          </p>
        </div>

        {error && (
          <div className="p-3.5 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900 text-xs text-rose-600 dark:text-rose-300 flex items-center space-x-2">
            <i className="fa-solid fa-triangle-exclamation"></i>
            <span>{error}</span>
          </div>
        )}

        {/* Login Form */}
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">Admin Email Address</label>
            <div className="relative">
              <span className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400 text-xs">
                <i className="fa-solid fa-envelope"></i>
              </span>
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="admin@example.com"
                className="w-full pl-9 pr-3 py-2.5 rounded-xl border border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-750 text-xs text-slate-900 dark:text-white font-medium focus:ring-2 focus:ring-[#22C55E] outline-hidden"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">Administrative Secret Key</label>
            <div className="relative">
              <span className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400 text-xs">
                <i className="fa-solid fa-lock"></i>
              </span>
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••••••"
                className="w-full pl-9 pr-3 py-2.5 rounded-xl border border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-750 text-xs text-slate-900 dark:text-white font-medium focus:ring-2 focus:ring-[#22C55E] outline-hidden"
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full py-3 rounded-xl bg-[#14532D] hover:bg-[#0f3d20] text-white font-black text-xs shadow-lg shadow-emerald-950/40 transition flex items-center justify-center space-x-2 cursor-pointer disabled:opacity-60"
          >
            {loading ? (
              <>
                <i className="fa-solid fa-circle-notch animate-spin"></i>
                <span>Authenticating JWT Credentials...</span>
              </>
            ) : (
              <>
                <i className="fa-solid fa-arrow-right-to-bracket"></i>
                <span>Secure Admin Login</span>
              </>
            )}
          </button>
        </form>

        <div className="text-center pt-2">
          <button
            onClick={onReturnToSite}
            className="text-xs font-bold text-slate-500 hover:text-emerald-600 transition flex items-center space-x-1.5 mx-auto"
          >
            <i className="fa-solid fa-arrow-left"></i>
            <span>Return to Public Website</span>
          </button>
        </div>
      </div>
    </div>
  );
};
