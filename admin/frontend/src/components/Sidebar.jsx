import React from 'react';

export const Sidebar = ({ activeTab, setActiveTab, onLogout, adminUser, collapsed, setCollapsed }) => {
  const menuItems = [
    { id: 'dashboard', label: 'Dashboard', icon: 'fa-chart-pie', badge: null },
    { id: 'users', label: 'User Management', icon: 'fa-users', badge: null },
    { id: 'predictions', label: 'AI Predictions', icon: 'fa-microscope', badge: 'Live' },
    { id: 'diseases', label: 'Disease Catalog', icon: 'fa-book-medical', badge: null },
    { id: 'organic', label: 'Organic Solutions', icon: 'fa-leaf', badge: null },
    { id: 'inorganic', label: 'Chemical Solutions', icon: 'fa-flask-vial', badge: null },
    { id: 'multilingual', label: 'Multilingual Content', icon: 'fa-language', badge: '7 Langs' },
    { id: 'models', label: 'ML Model Monitoring', icon: 'fa-brain', badge: 'v2.4' },
    { id: 'feedback', label: 'Feedback & Support', icon: 'fa-comments', badge: null },
    { id: 'notifications', label: 'Announcements', icon: 'fa-bullhorn', badge: null },
    { id: 'reports', label: 'Reports & Analytics', icon: 'fa-file-invoice', badge: 'PDF/CSV' },
    { id: 'settings', label: 'System Settings', icon: 'fa-gear', badge: null },
    { id: 'audit', label: 'Admin Activity Logs', icon: 'fa-shield-halved', badge: 'Audit' },
  ];

  return (
    <aside className={`transition-all duration-300 ${collapsed ? 'w-20' : 'w-72'} bg-[#14532D] text-white flex flex-col justify-between shrink-0 shadow-2xl z-40 relative`}>
      {/* Top Brand Header */}
      <div>
        <div className="p-5 flex items-center justify-between border-b border-emerald-800/60">
          <div className="flex items-center space-x-3 overflow-hidden">
            <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-[#22C55E] to-emerald-400 text-[#14532D] flex items-center justify-center text-xl font-black shadow-md shrink-0">
              <i className="fa-solid fa-leaf"></i>
            </div>
            {!collapsed && (
              <div className="truncate">
                <h1 className="font-black text-lg tracking-tight leading-tight text-white flex items-center space-x-1.5">
                  <span>AGROCURE</span>
                  <span className="text-[#22C55E]">ADMIN</span>
                </h1>
                <p className="text-[10px] font-mono uppercase text-emerald-300 tracking-wider">Enterprise Console</p>
              </div>
            )}
          </div>
          <button
            onClick={() => setCollapsed(!collapsed)}
            className="text-emerald-300 hover:text-white p-1.5 rounded-lg hover:bg-emerald-800/40 transition text-xs"
          >
            <i className={`fa-solid ${collapsed ? 'fa-chevron-right' : 'fa-chevron-left'}`}></i>
          </button>
        </div>

        {/* Menu Navigation Items */}
        <nav className="p-3 space-y-1 overflow-y-auto max-h-[calc(100vh-210px)] scrollbar-thin">
          {menuItems.map(item => {
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => setActiveTab(item.id)}
                title={collapsed ? item.label : undefined}
                className={`w-full flex items-center ${collapsed ? 'justify-center px-2' : 'justify-between px-3.5'} py-2.5 rounded-xl text-xs font-bold transition-all duration-150 ${
                  isActive
                    ? 'bg-[#22C55E] text-[#14532D] shadow-md font-extrabold'
                    : 'text-emerald-100 hover:bg-emerald-800/50 hover:text-white'
                }`}
              >
                <div className="flex items-center space-x-3 truncate">
                  <i className={`fa-solid ${item.icon} ${collapsed ? 'text-lg' : 'text-sm'} w-5 text-center`}></i>
                  {!collapsed && <span className="truncate">{item.label}</span>}
                </div>
                {!collapsed && item.badge && (
                  <span className={`text-[10px] px-2 py-0.5 rounded-full font-mono font-bold uppercase ${
                    isActive ? 'bg-[#14532D] text-white' : 'bg-emerald-900/80 text-emerald-300 border border-emerald-700/60'
                  }`}>
                    {item.badge}
                  </span>
                )}
              </button>
            );
          })}
        </nav>
      </div>

      {/* Admin Profile & Logout Bar */}
      <div className="p-4 border-t border-emerald-800/60 bg-emerald-950/60">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3 overflow-hidden">
            <img
              src={adminUser?.avatar || '/static/team/dev1.png'}
              alt="Admin Avatar"
              className="w-9 h-9 rounded-xl object-cover ring-2 ring-[#22C55E] shrink-0"
            />
            {!collapsed && (
              <div className="truncate">
                <div className="text-xs font-bold text-white truncate">{adminUser?.name || 'Administrator'}</div>
                <div className="text-[10px] text-emerald-300 font-mono truncate">{adminUser?.role || 'Super Admin'}</div>
              </div>
            )}
          </div>
          <button
            onClick={onLogout}
            title="Log out from Admin Panel"
            className="w-8 h-8 rounded-xl bg-red-500/20 text-red-300 hover:bg-red-500 hover:text-white flex items-center justify-center text-xs transition shrink-0 ml-2 shadow-xs"
          >
            <i className="fa-solid fa-right-from-bracket"></i>
          </button>
        </div>
      </div>
    </aside>
  );
};
