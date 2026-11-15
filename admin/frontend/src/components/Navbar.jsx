import React from 'react';

export const Navbar = ({ adminUser, onLogout, toggleTheme, theme, onReturnToSite }) => {
  return (
    <header className="h-16 bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 px-6 flex items-center justify-between shadow-xs z-30">
      {/* Search & Breadcrumb */}
      <div className="flex items-center space-x-4">
        <span className="px-2.5 py-1 rounded-full bg-emerald-100 dark:bg-emerald-950 text-[#14532D] dark:text-emerald-300 text-[11px] font-black uppercase tracking-wider flex items-center space-x-1.5">
          <span className="w-2 h-2 rounded-full bg-[#22C55E] animate-ping"></span>
          <span>SYSTEM ONLINE</span>
        </span>
        <span className="text-xs text-slate-500 font-medium hidden sm:inline">
          Server: <strong className="text-slate-800 dark:text-white">v2.4.1 (MobileNetV2 + OpenCV)</strong>
        </span>
      </div>

      {/* Action Controls */}
      <div className="flex items-center space-x-3">
        {/* Return to Public Website */}
        <button
          onClick={onReturnToSite}
          className="px-3.5 py-1.5 rounded-xl border border-emerald-600/30 hover:border-emerald-600 bg-emerald-50 dark:bg-emerald-950/40 text-[#14532D] dark:text-emerald-300 text-xs font-bold flex items-center space-x-1.5 transition shadow-xs"
        >
          <i className="fa-solid fa-arrow-left"></i>
          <span className="hidden md:inline">Public Website</span>
        </button>

        {/* Theme Toggle */}
        <button
          onClick={toggleTheme}
          title="Toggle Dark / Light Theme"
          className="w-9 h-9 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex items-center justify-center text-xs hover:bg-slate-200 dark:hover:bg-slate-700 transition"
        >
          <i className={`fa-solid ${theme === 'dark' ? 'fa-sun text-amber-400' : 'fa-moon text-indigo-500'}`}></i>
        </button>

        {/* Admin Badge */}
        <div className="flex items-center space-x-2.5 pl-2 border-l border-slate-200 dark:border-slate-800">
          <img
            src={adminUser?.avatar || '/static/team/dev1.png'}
            alt="Admin"
            className="w-8 h-8 rounded-lg object-cover ring-2 ring-[#22C55E]"
          />
          <div className="hidden lg:block text-left">
            <span className="text-xs font-black text-slate-900 dark:text-white block leading-tight">{adminUser?.name || 'Administrator'}</span>
            <span className="text-[10px] font-bold text-emerald-600 dark:text-emerald-400 uppercase">{adminUser?.role || 'Super Admin'}</span>
          </div>
        </div>
      </div>
    </header>
  );
};
