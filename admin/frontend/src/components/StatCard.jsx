import React from 'react';

export const StatCard = ({ title, value, change, icon, iconBg, iconColor, subtitle }) => {
  return (
    <div className="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700/80 rounded-2xl p-5 shadow-xs hover:shadow-md transition-shadow relative overflow-hidden">
      <div className="flex items-center justify-between">
        <div>
          <span className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider block">{title}</span>
          <div className="text-2xl sm:text-3xl font-black text-slate-900 dark:text-white mt-1 font-mono tracking-tight">{value}</div>
          {subtitle && <p className="text-[11px] text-slate-400 mt-0.5">{subtitle}</p>}
        </div>
        <div className={`w-12 h-12 rounded-2xl ${iconBg || 'bg-emerald-100 dark:bg-emerald-950'} ${iconColor || 'text-[#14532D] dark:text-[#22C55E]'} flex items-center justify-center text-xl shadow-inner shrink-0`}>
          <i className={`fa-solid ${icon}`}></i>
        </div>
      </div>
      {change !== undefined && (
        <div className="mt-3 pt-2.5 border-t border-slate-100 dark:border-slate-700/60 flex items-center space-x-1.5 text-xs font-bold">
          <span className="text-[#22C55E] flex items-center space-x-1">
            <i className="fa-solid fa-arrow-trend-up"></i>
            <span>{change}</span>
          </span>
          <span className="text-slate-400 font-normal">vs previous cycle</span>
        </div>
      )}
    </div>
  );
};
