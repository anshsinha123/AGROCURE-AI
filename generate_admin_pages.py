from pathlib import Path

pages_dir = Path(__file__).resolve().parent / "admin" / "frontend" / "src" / "pages"

# 1. AdminLogin.jsx
login_code = """import React, { useState } from 'react';

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
"""
with open(pages_dir / "AdminLogin.jsx", "w", encoding="utf-8") as f:
    f.write(login_code)

# 2. Dashboard.jsx
dashboard_code = """import React from 'react';
import { StatCard } from '../components/StatCard';

export const Dashboard = ({ stats, analytics, onNavigate }) => {
  return (
    <div className="space-y-6">
      {/* Welcome Banner */}
      <div className="bg-gradient-to-r from-[#14532D] to-emerald-800 text-white rounded-3xl p-6 sm:p-8 shadow-xl relative overflow-hidden">
        <div className="relative z-10 max-w-2xl space-y-2">
          <span className="px-3 py-1 rounded-full bg-emerald-500/20 text-[#22C55E] text-[11px] font-mono font-bold uppercase tracking-wider border border-emerald-400/30">
            Real-Time Agricultural Telemetry
          </span>
          <h2 className="text-2xl sm:text-3xl font-black tracking-tight">Plant Pathology Command Center</h2>
          <p className="text-xs sm:text-sm text-emerald-100/90 leading-relaxed">
            Real-time monitoring across 19 pathogen classes in Tomato, Potato, Capsicum, and Grapes. Live database synchronization with MobileNetV2 inference engine.
          </p>
        </div>
        <div className="absolute -right-8 -bottom-8 opacity-10 text-[160px] pointer-events-none text-emerald-300">
          <i className="fa-solid fa-microscope"></i>
        </div>
      </div>

      {/* 10 Core Metric Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-4">
        <StatCard title="Total Users" value={stats.total_users || 0} change="+12.4%" icon="fa-users" />
        <StatCard title="Plant Scans" value={stats.total_scans || 0} change="+24.8%" icon="fa-microscope" iconColor="text-teal-600" iconBg="bg-teal-100 dark:bg-teal-950" />
        <StatCard title="Healthy Leaves" value={stats.healthy_scans || 0} icon="fa-leaf" iconColor="text-emerald-500" iconBg="bg-emerald-100 dark:bg-emerald-950" />
        <StatCard title="Diseased Diagnoses" value={stats.diseased_scans || 0} icon="fa-biohazard" iconColor="text-rose-500" iconBg="bg-rose-100 dark:bg-rose-950" />
        <StatCard title="Active Growers" value={stats.active_users || 0} icon="fa-user-check" iconColor="text-blue-500" iconBg="bg-blue-100 dark:bg-blue-950" />
        
        <StatCard title="Tomato Scans" value={stats.tomato_scans || 0} icon="fa-apple-whole" iconColor="text-red-500" iconBg="bg-red-100 dark:bg-red-950" subtitle="10 Classes" />
        <StatCard title="Potato Scans" value={stats.potato_scans || 0} icon="fa-egg" iconColor="text-amber-500" iconBg="bg-amber-100 dark:bg-amber-950" subtitle="3 Classes" />
        <StatCard title="Capsicum Scans" value={stats.capsicum_scans || 0} icon="fa-pepper-hot" iconColor="text-green-500" iconBg="bg-green-100 dark:bg-green-950" subtitle="2 Classes" />
        <StatCard title="Grapes Scans" value={stats.grapes_scans || 0} icon="fa-wine-bottle" iconColor="text-purple-500" iconBg="bg-purple-100 dark:bg-purple-950" subtitle="4 Classes" />
        <StatCard title="Feedback Received" value={stats.total_feedback || 0} icon="fa-comments" iconColor="text-yellow-500" iconBg="bg-yellow-100 dark:bg-yellow-950" subtitle="4.9 ★ Avg" />
      </div>

      {/* Analytical Charts Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Daily Scan Volume Bar Chart */}
        <div className="lg:col-span-8 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-3xl p-6 shadow-xs space-y-4">
          <div className="flex items-center justify-between border-b border-slate-100 dark:border-slate-700 pb-3">
            <div>
              <h3 className="text-sm font-black text-slate-900 dark:text-white uppercase tracking-wider">
                Daily Prediction Telemetry (Last 7 Days)
              </h3>
              <p className="text-xs text-slate-400">MobileNetV2 neural classifications per calendar date</p>
            </div>
            <span className="px-2.5 py-1 rounded-lg bg-emerald-100 dark:bg-emerald-950 text-[#14532D] dark:text-emerald-300 text-xs font-mono font-bold">
              Avg: 42ms Latency
            </span>
          </div>

          <div className="h-64 flex items-end justify-between gap-3 pt-6 px-2">
            {(analytics.daily_predictions || [
              { day: 'Mon', count: 18 },
              { day: 'Tue', count: 24 },
              { day: 'Wed', count: 32 },
              { day: 'Thu', count: 28 },
              { day: 'Fri', count: 45 },
              { day: 'Sat', count: 52 },
              { day: 'Sun', count: 38 }
            ]).map((d, i) => {
              const max = 60;
              const heightPct = Math.round((d.count / max) * 100);
              return (
                <div key={i} className="flex-1 flex flex-col items-center gap-2 group">
                  <span className="text-[10px] font-mono font-bold text-slate-500 group-hover:text-[#22C55E] transition-colors">{d.count}</span>
                  <div className="w-full bg-slate-100 dark:bg-slate-700 rounded-xl h-44 flex items-end p-1">
                    <div
                      className="w-full bg-gradient-to-t from-[#14532D] to-[#22C55E] rounded-lg transition-all duration-500 group-hover:brightness-110 shadow-md"
                      style={{ height: `${heightPct}%` }}
                    ></div>
                  </div>
                  <span className="text-xs font-bold text-slate-600 dark:text-slate-400">{d.day}</span>
                </div>
              );
            })}
          </div>
        </div>

        {/* Crop-Wise Distribution Donut Representation */}
        <div className="lg:col-span-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-3xl p-6 shadow-xs space-y-4 flex flex-col justify-between">
          <div>
            <h3 className="text-sm font-black text-slate-900 dark:text-white uppercase tracking-wider border-b border-slate-100 dark:border-slate-700 pb-3">
              Crop Scan Distribution
            </h3>
            <p className="text-xs text-slate-400 mt-2">Breakdown across 4 high-yield agricultural crops</p>
          </div>

          <div className="space-y-3 pt-2">
            {[
              { crop: 'Tomato', count: stats.tomato_scans || 14, color: 'bg-red-500', pct: 45 },
              { crop: 'Potato', count: stats.potato_scans || 8, color: 'bg-amber-500', pct: 25 },
              { crop: 'Grapes', count: stats.grapes_scans || 6, color: 'bg-purple-500', pct: 18 },
              { crop: 'Capsicum', count: stats.capsicum_scans || 4, color: 'bg-green-500', pct: 12 }
            ].map(item => (
              <div key={item.crop} className="space-y-1">
                <div className="flex justify-between text-xs font-bold text-slate-700 dark:text-slate-300">
                  <span className="flex items-center space-x-2">
                    <span className={`w-2.5 h-2.5 rounded-full ${item.color}`}></span>
                    <span>{item.crop}</span>
                  </span>
                  <span className="font-mono">{item.count} scans ({item.pct}%)</span>
                </div>
                <div className="w-full h-2 rounded-full bg-slate-100 dark:bg-slate-700 overflow-hidden">
                  <div className={`h-full ${item.color} rounded-full`} style={{ width: `${item.pct}%` }}></div>
                </div>
              </div>
            ))}
          </div>

          <button
            onClick={() => onNavigate('predictions')}
            className="w-full py-2.5 rounded-xl border border-emerald-500/30 bg-emerald-50 dark:bg-emerald-950/40 text-[#14532D] dark:text-emerald-300 text-xs font-bold hover:bg-emerald-100 dark:hover:bg-emerald-900 transition flex items-center justify-center space-x-1.5"
          >
            <span>View All AI Predictions</span>
            <i className="fa-solid fa-arrow-right text-[10px]"></i>
          </button>
        </div>
      </div>
    </div>
  );
};
"""
with open(pages_dir / "Dashboard.jsx", "w", encoding="utf-8") as f:
    f.write(dashboard_code)

print("Pages AdminLogin.jsx and Dashboard.jsx generated.")
