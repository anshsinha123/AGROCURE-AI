import React, { useState } from 'react';

export const Users = ({ users, onUpdateStatus, onDeleteUser, onExportCSV }) => {
  const [search, setSearch] = useState('');
  const [roleFilter, setRoleFilter] = useState('All');
  const [statusFilter, setStatusFilter] = useState('All');
  const [selectedUser, setSelectedUser] = useState(null);

  const filteredUsers = users.filter(u => {
    const matchesSearch = (u.name || '').toLowerCase().includes(search.toLowerCase()) ||
                          (u.email || '').toLowerCase().includes(search.toLowerCase()) ||
                          (u.farm_location || '').toLowerCase().includes(search.toLowerCase());
    const matchesRole = roleFilter === 'All' || u.role === roleFilter;
    const matchesStatus = statusFilter === 'All' || (u.status || 'Active') === statusFilter;
    return matchesSearch && matchesRole && matchesStatus;
  });

  return (
    <div className="space-y-6">
      {/* Top Header & Actions */}
      <div className="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-3xl p-6 shadow-xs flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-black text-slate-900 dark:text-white flex items-center space-x-2">
            <i className="fa-solid fa-users text-[#22C55E]"></i>
            <span>User & Grower Management</span>
          </h2>
          <p className="text-xs text-slate-400 mt-1">
            Registered farmers, agronomists, and researchers. Password hashes are strictly secured.
          </p>
        </div>

        <button
          onClick={onExportCSV}
          className="px-4 py-2.5 rounded-xl bg-[#14532D] hover:bg-[#0f3d20] text-white text-xs font-bold transition flex items-center space-x-2 shadow-md shrink-0"
        >
          <i className="fa-solid fa-file-csv"></i>
          <span>Export Users (CSV)</span>
        </button>
      </div>

      {/* Filter Toolbar */}
      <div className="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-2xl p-4 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div className="relative flex-1">
          <span className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400 text-xs">
            <i className="fa-solid fa-magnifying-glass"></i>
          </span>
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search by name, email, or farm location..."
            className="w-full pl-9 pr-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-750 text-xs text-slate-900 dark:text-white font-medium focus:ring-2 focus:ring-[#22C55E] outline-hidden"
          />
        </div>

        <div className="flex items-center space-x-2 shrink-0">
          <select
            value={roleFilter}
            onChange={(e) => setRoleFilter(e.target.value)}
            className="px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-750 text-xs font-bold text-slate-700 dark:text-slate-200"
          >
            <option value="All">All Roles</option>
            <option value="Farmer">Farmer</option>
            <option value="Agronomist">Agronomist</option>
            <option value="Researcher">Researcher</option>
            <option value="Student">Student</option>
            <option value="Developer">Developer</option>
          </select>

          <select
            value={statusFilter}
            onChange={(e) => setStatusFilter(e.target.value)}
            className="px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-750 text-xs font-bold text-slate-700 dark:text-slate-200"
          >
            <option value="All">All Statuses</option>
            <option value="Active">Active</option>
            <option value="Suspended">Suspended</option>
          </select>
        </div>
      </div>

      {/* Users Data Table */}
      <div className="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-3xl overflow-hidden shadow-xs">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-50 dark:bg-slate-750 border-b border-slate-200 dark:border-slate-700 text-slate-500 uppercase font-mono text-[10px]">
              <tr>
                <th className="px-5 py-3.5">User</th>
                <th className="px-4 py-3.5">Role</th>
                <th className="px-4 py-3.5">Farm Location</th>
                <th className="px-4 py-3.5">Primary Crop</th>
                <th className="px-4 py-3.5">Status</th>
                <th className="px-4 py-3.5">Joined</th>
                <th className="px-5 py-3.5 text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100 dark:divide-slate-700/60 font-medium">
              {filteredUsers.length === 0 ? (
                <tr>
                  <td colSpan="7" className="text-center py-8 text-slate-400">
                    No users matching search filters found.
                  </td>
                </tr>
              ) : (
                filteredUsers.map((u) => {
                  const isActive = (u.status || 'Active') === 'Active';
                  return (
                    <tr key={u.id} className="hover:bg-slate-50/50 dark:hover:bg-slate-750/50 transition-colors">
                      <td className="px-5 py-3.5">
                        <div className="flex items-center space-x-3">
                          <img
                            src={u.avatar || '/static/team/dev1.png'}
                            alt=""
                            className="w-8 h-8 rounded-lg object-cover ring-1 ring-slate-300 dark:ring-slate-700"
                          />
                          <div>
                            <span className="font-bold text-slate-900 dark:text-white block">{u.name}</span>
                            <span className="text-[11px] text-slate-400 block">{u.email}</span>
                          </div>
                        </div>
                      </td>
                      <td className="px-4 py-3.5">
                        <span className="px-2 py-0.5 rounded-md bg-emerald-100 dark:bg-emerald-950/60 text-[#14532D] dark:text-emerald-300 font-bold text-[10px]">
                          {u.role || 'Farmer'}
                        </span>
                      </td>
                      <td className="px-4 py-3.5 text-slate-600 dark:text-slate-300">{u.farm_location || 'General'}</td>
                      <td className="px-4 py-3.5 font-bold text-slate-700 dark:text-slate-300">{u.preferred_crop || 'Tomato'}</td>
                      <td className="px-4 py-3.5">
                        <span className={`px-2 py-0.5 rounded-full text-[10px] font-mono font-bold uppercase ${
                          isActive
                            ? 'bg-emerald-500/10 text-emerald-600 border border-emerald-500/30'
                            : 'bg-rose-500/10 text-rose-600 border border-rose-500/30'
                        }`}>
                          {isActive ? 'Active' : 'Suspended'}
                        </span>
                      </td>
                      <td className="px-4 py-3.5 text-slate-400 font-mono text-[11px]">{u.created_at ? u.created_at.slice(0, 10) : '2026-01-15'}</td>
                      <td className="px-5 py-3.5 text-right space-x-2">
                        <button
                          onClick={() => setSelectedUser(u)}
                          className="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-700 hover:bg-slate-200 text-slate-700 dark:text-slate-200 font-bold text-[11px]"
                          title="View Profile"
                        >
                          View
                        </button>
                        <button
                          onClick={() => onUpdateStatus(u.id, isActive ? 'Suspended' : 'Active')}
                          className={`px-2.5 py-1 rounded-lg text-[11px] font-bold ${
                            isActive
                              ? 'bg-amber-100 text-amber-800 hover:bg-amber-200'
                              : 'bg-emerald-100 text-emerald-800 hover:bg-emerald-200'
                          }`}
                        >
                          {isActive ? 'Suspend' : 'Activate'}
                        </button>
                        <button
                          onClick={() => {
                            if (window.confirm(`Delete account for ${u.name}? This action is irreversible.`)) {
                              onDeleteUser(u.id);
                            }
                          }}
                          className="px-2 py-1 rounded-lg text-rose-600 hover:bg-rose-50 dark:hover:bg-rose-950/40 text-[11px]"
                          title="Delete User"
                        >
                          <i className="fa-solid fa-trash"></i>
                        </button>
                      </td>
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* User Profile Detail Modal */}
      {selectedUser && (
        <div className="fixed inset-0 z-50 bg-slate-950/70 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-3xl max-w-lg w-full p-6 space-y-4 shadow-2xl relative">
            <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-700 pb-3">
              <h3 className="font-black text-base text-slate-900 dark:text-white">Grower Profile Inspection</h3>
              <button onClick={() => setSelectedUser(null)} className="text-slate-400 hover:text-white">
                <i className="fa-solid fa-xmark"></i>
              </button>
            </div>
            <div className="flex items-center space-x-4">
              <img src={selectedUser.avatar || '/static/team/dev1.png'} className="w-16 h-16 rounded-2xl object-cover ring-2 ring-emerald-500" alt="" />
              <div>
                <h4 className="text-base font-bold text-slate-900 dark:text-white">{selectedUser.name}</h4>
                <p className="text-xs text-slate-400">{selectedUser.email}</p>
                <span className="mt-1 inline-block px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300">
                  {selectedUser.role} &bull; {selectedUser.status || 'Active'}
                </span>
              </div>
            </div>
            <div className="grid grid-cols-2 gap-3 text-xs bg-slate-50 dark:bg-slate-750 p-4 rounded-2xl">
              <div><strong>Farm Location:</strong> {selectedUser.farm_location || 'N/A'}</div>
              <div><strong>Acreage:</strong> {selectedUser.farm_size || 'N/A'}</div>
              <div><strong>Main Crop:</strong> {selectedUser.preferred_crop || 'Tomato'}</div>
              <div><strong>Dialect:</strong> {(selectedUser.preferred_lang || 'en').toUpperCase()}</div>
              <div><strong>Phone:</strong> {selectedUser.phone || 'Not provided'}</div>
              <div><strong>Bio:</strong> {selectedUser.bio || 'Registered cultivator'}</div>
            </div>
            <div className="text-right pt-2">
              <button onClick={() => setSelectedUser(null)} className="px-4 py-2 bg-slate-100 dark:bg-slate-700 font-bold text-xs rounded-xl text-slate-700 dark:text-slate-300">
                Close Inspector
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
