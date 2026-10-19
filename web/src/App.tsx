import React, { useState } from 'react';
import { SmsSyncService } from './SmsSyncService';

export default function App() {
  const [smsBody, setSmsBody] = useState('YOUR A/C XX4321 HAS BEEN DEBITED FOR RS. 1,250.50 VIA UPI TO SWIGGY@HDFCBANK ON 19-10-2026.');
  const [sender, setSender] = useState('AD-HDFCBK');
  const [token, setToken] = useState('MOCK_JWT_ACCESS_TOKEN');
  const [statusMessage, setStatusMessage] = useState<string | null>(null);
  const [parsedData, setParsedData] = useState<any | null>(null);

  const apiService = new SmsSyncService('http://localhost:8000');

  const handleManualIngestion = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatusMessage('Processing text data payload...');
    setParsedData(null);

    try {
      const res = await apiService.triggerSmsSync({
        sender,
        body: smsBody,
        timestamp: new Date().toISOString(),
        sim_slot: 0
      }, token);

      setStatusMessage('✓ Ledger entry verified and compiled successfully!');
      setParsedData(res.data);
    } catch (err: any) {
      setStatusMessage(`✕ Sync Error: ${err.message || err}`);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 font-sans text-gray-900">
      <header className="bg-emerald-700 text-white p-4 shadow-md">
        <h1 className="text-xl font-bold tracking-wide">🇮🇳 Indian Personal Finance Ledger Management Console</h1>
      </header>
      
      <main className="max-w-4xl mx-auto p-6 grid grid-cols-1 md:grid-cols-2 gap-6">
        <section className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <h2 className="text-lg font-semibold mb-4 text-emerald-800">QuickBooks-Style Transaction Ingestion</h2>
          <form onSubmit={handleManualIngestion} className="space-y-4">
            <div>
              <label className="block text-xs font-bold uppercase text-gray-500 mb-1">Sender Handle</label>
              <input type="text" className="w-full border p-2 rounded" value={sender} onChange={e => setSender(e.target.value)} />
            </div>
            <div>
              <label className="block text-xs font-bold uppercase text-gray-500 mb-1">Banking SMS String Text</label>
              <textarea rows={4} className="w-full border p-2 rounded text-sm font-mono" value={smsBody} onChange={e => setSmsBody(e.target.value)} />
            </div>
            <button type="submit" className="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-medium p-2 rounded transition">
              Process Transaction Ledger Split
            </button>
          </form>
        </section>

        <section className="bg-white p-6 rounded-lg shadow-sm border border-gray-200 flex flex-col justify-between">
          <div>
            <h2 className="text-lg font-semibold mb-4 text-gray-700">Real-Time Compilation Summary</h2>
            {statusMessage && (
              <div className={`p-3 rounded mb-4 text-sm font-medium ${statusMessage.startsWith('✓') ? 'bg-emerald-50 text-emerald-800' : 'bg-red-50 text-red-800'}`}>
                {statusMessage}
              </div>
            )}
            {parsedData && (
              <div className="bg-gray-900 text-emerald-400 p-4 rounded font-mono text-xs space-y-2">
                <p><span className="text-gray-400">Captured Amount :</span> ₹{parsedData.amount}</p>
                <p><span className="text-gray-400">Direction Type   :</span> {parsedData.action}</p>
                <p><span className="text-gray-400">Source Registry  :</span> {parsedData.account_source}</p>
                <p><span className="text-gray-400">Destination VPA  :</span> {parsedData.merchant_ref}</p>
              </div>
            )}
          </div>
          <div className="border-t pt-4 text-xs text-gray-400 text-center">
            Double-Entry Balancing Validation Status: <span className="text-emerald-600 font-bold">RECONCILED (0.00)</span>
          </div>
        </section>
      </main>
    </div>
  );
}
