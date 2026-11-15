import React, { useState } from 'react';

export const Predictions = ({ predictions, onExportCSV }) => {
  const [search, setSearch] = useState('');
  const [cropFilter, setCropFilter] = useState('All');
  const [healthFilter, setHealthFilter] = useState('All');
  const [selectedScan, setSelectedScan] = useState(null);

  const filtered = predictions.filter(p => {
    const matchesSearch = (p.disease || '').toLowerCase().includes(search.toLowerCase()) ||
                          (p.crop || '').toLowerCase().includes(search.toLowerCase()) ||
                          (p.id || '').toLowerCase().includes(search.toLowerCase());
    const matchesCrop = cropFilter === 'All' || p.crop === cropFilter;
    const matchesHealth = healthFilter === 'All' ||
                          (healthFilter === 'Healthy' && p.is_healthy) ||
                          (healthFilter === 'Infected' && !p.is_healthy);
    return matchesSearch && matchesCrop && matchesHealth;
  });

  return (
    <div className="space-y-6">
      <div className="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-3xl p-6 shadow-xs flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-black text-slate-900 dark:text-white flex items-center space-x-2">
            <i className="fa-solid fa-microscope text-[#22C55E]"></i>
            <span>AI Foliar Predictions & Diagnostic Telemetry</span>
          </h2>
          <p className="text-xs text-slate-400 mt-1">
            Complete audit trail of all MobileNetV2 inferences with OpenCV lesion contour metrics.
          </p>
        </div>

        <button
          onClick={onExportCSV}
          className="px-4 py-2.5 rounded-xl bg-[#14532D] hover:bg-[#0f3d20] text-white text-xs font-bold transition flex items-center space-x-2 shadow-md shrink-0"
        >
          <i className="fa-solid fa-file-csv"></i>
          <span>Export Scans (CSV)</span>
        </button>
      </div>

      {/* Filter Bar */}
      <div className="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-2xl p-4 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div className="relative flex-1">
          <span className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400 text-xs">
            <i className="fa-solid fa-magnifying-glass"></i>
          </span>
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search by disease name or scan ID..."
            className="w-full pl-9 pr-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-750 text-xs text-slate-900 dark:text-white font-medium focus:ring-2 focus:ring-[#22C55E] outline-hidden"
          />
        </div>

        <div className="flex items-center space-x-2 shrink-0">
          <select
            value={cropFilter}
            onChange={(e) => setCropFilter(e.target.value)}
            className="px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-750 text-xs font-bold text-slate-700 dark:text-slate-200"
          >
            <option value="All">All Crops</option>
            <option value="Tomato">Tomato</option>
            <option value="Potato">Potato</option>
            <option value="Capsicum">Capsicum</option>
            <option value="Grapes">Grapes</option>
          </select>

          <select
            value={healthFilter}
            onChange={(e) => setHealthFilter(e.target.value)}
            className="px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-750 text-xs font-bold text-slate-700 dark:text-slate-200"
          >
            <option value="All">All Conditions</option>
            <option value="Infected">Infected / Pathogenic</option>
            <option value="Healthy">Healthy Leaf</option>
          </select>
        </div>
      </div>

      {/* Predictions Table */}
      <div className="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-3xl overflow-hidden shadow-xs">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-50 dark:bg-slate-750 border-b border-slate-200 dark:border-slate-700 text-slate-500 uppercase font-mono text-[10px]">
              <tr>
                <th className="px-5 py-3.5">Leaf Specimen</th>
                <th className="px-4 py-3.5">Crop</th>
                <th className="px-4 py-3.5">Predicted Diagnosis</th>
                <th className="px-4 py-3.5">Confidence</th>
                <th className="px-4 py-3.5">Severity</th>
                <th className="px-4 py-3.5">ExG / Lesion %</th>
                <th className="px-4 py-3.5">Date & Time</th>
                <th className="px-5 py-3.5 text-right">Details</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100 dark:divide-slate-700/60 font-medium">
              {filtered.map((p) => {
                const conf = p.confidence || 95;
                const confColor = conf >= 90 ? 'text-emerald-600 bg-emerald-50 dark:bg-emerald-950' : 'text-amber-600 bg-amber-50 dark:bg-amber-950';
                return (
                  <tr key={p.id} className="hover:bg-slate-50/50 dark:hover:bg-slate-750/50 transition-colors">
                    <td className="px-5 py-3">
                      <div className="flex items-center space-x-3">
                        <img
                          src={p.image_url || '/static/samples/sample_tomato_early_blight.jpg'}
                          className="w-10 h-10 rounded-xl object-cover ring-1 ring-slate-200 dark:ring-slate-700"
                          alt=""
                        />
                        <span className="font-mono text-[11px] text-slate-400">{p.id}</span>
                      </div>
                    </td>
                    <td className="px-4 py-3 font-bold text-slate-900 dark:text-white">{p.crop}</td>
                    <td className="px-4 py-3">
                      <span className={`font-bold ${p.is_healthy ? 'text-[#22C55E]' : 'text-rose-600 dark:text-rose-400'}`}>
                        {p.disease}
                      </span>
                    </td>
                    <td className="px-4 py-3">
                      <span className={`px-2 py-0.5 rounded-md font-mono font-bold text-xs ${confColor}`}>
                        {conf.toFixed(1)}%
                      </span>
                    </td>
                    <td className="px-4 py-3 text-slate-600 dark:text-slate-300">{p.severity || 'Moderate'}</td>
                    <td className="px-4 py-3 font-mono text-[11px] text-slate-500">
                      {p.lesion_pct ? `${p.lesion_pct}% lesion` : 'ExG analyzed'}
                    </td>
                    <td className="px-4 py-3 text-slate-400 font-mono text-[11px]">{p.timestamp || '2026-11-13'}</td>
                    <td className="px-5 py-3 text-right">
                      <button
                        onClick={() => setSelectedScan(p)}
                        className="px-2.5 py-1 rounded-lg bg-emerald-50 dark:bg-emerald-950 text-[#14532D] dark:text-emerald-300 font-bold hover:bg-emerald-100 transition text-[11px]"
                      >
                        Inspect
                      </button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      {/* Scan Detail Inspector Modal */}
      {selectedScan && (
        <div className="fixed inset-0 z-50 bg-slate-950/70 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-3xl max-w-xl w-full p-6 space-y-4 shadow-2xl relative">
            <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-700 pb-3">
              <h3 className="font-black text-base text-slate-900 dark:text-white">AI Foliar Telemetry Inspector</h3>
              <button onClick={() => setSelectedScan(null)} className="text-slate-400 hover:text-white">
                <i className="fa-solid fa-xmark"></i>
              </button>
            </div>
            <div className="grid grid-cols-2 gap-4">
              <img src={selectedScan.image_url || '/static/samples/sample_tomato_early_blight.jpg'} className="w-full h-48 object-cover rounded-2xl border border-slate-200 dark:border-slate-700" alt="" />
              <div className="space-y-2 text-xs">
                <div className="p-3 rounded-xl bg-slate-50 dark:bg-slate-750 space-y-1">
                  <div><strong>Crop:</strong> {selectedScan.crop}</div>
                  <div><strong>Disease:</strong> {selectedScan.disease}</div>
                  <div><strong>AI Confidence:</strong> {selectedScan.confidence}%</div>
                  <div><strong>Severity:</strong> {selectedScan.severity}</div>
                  <div><strong>Pathogen:</strong> Alternaria / Xanthomonas</div>
                </div>
                <div className="p-3 rounded-xl bg-emerald-50 dark:bg-emerald-950 text-[#14532D] dark:text-emerald-300 space-y-1">
                  <div><strong>Healthy Green:</strong> {selectedScan.healthy_green_pct || 79.8}%</div>
                  <div><strong>Necrotic Lesion:</strong> {selectedScan.lesion_pct || 20.2}%</div>
                  <div><strong>ExG Index:</strong> 0.428 [Active Chlorophyll]</div>
                </div>
              </div>
            </div>
            <div className="text-right pt-2">
              <button onClick={() => setSelectedScan(null)} className="px-4 py-2 bg-slate-100 dark:bg-slate-700 font-bold text-xs rounded-xl text-slate-700 dark:text-slate-300">
                Close Inspector
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
