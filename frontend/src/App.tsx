import { useState, useEffect } from 'react'
import { Sun, Shield, Zap, Info, AlertTriangle, RefreshCw } from 'lucide-react'

interface SpaceData {
  [key: string]: any;
}

function App() {
  const [aIndex, setAIndex] = useState<SpaceData | null>(null)
  const [kIndex, setKIndex] = useState<SpaceData | null>(null)
  const [dstIndex, setDstIndex] = useState<SpaceData | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  const fetchData = async () => {
    setLoading(true)
    setError(null)
    try {
      const baseUrl = 'http://localhost:8000/api'
      const [a, k, dst] = await Promise.all([
        fetch(`${baseUrl}/a-index`).then(res => res.json()),
        fetch(`${baseUrl}/k-index`).then(res => res.json()),
        fetch(`${baseUrl}/dst-index`).then(res => res.json())
      ])
      setAIndex(a)
      setKIndex(k)
      setDstIndex(dst)
    } catch (err) {
      setError('Failed to fetch space weather data. Is the backend running?')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchData()
  }, [])

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-8">
      <header className="max-w-6xl mx-auto mb-12 flex justify-between items-center">
        <div>
          <h1 className="text-4xl font-bold bg-gradient-to-r from-blue-400 to-emerald-400 bg-clip-text text-transparent">
            Space Weather Dashboard
          </h1>
          <p className="text-slate-400 mt-2">Real-time solar and geomagnetic activity monitoring</p>
        </div>
        <button 
          onClick={fetchData}
          className="p-2 bg-slate-800 hover:bg-slate-700 rounded-lg transition-colors flex items-center gap-2"
          disabled={loading}
        >
          <RefreshCw className={`w-5 h-5 ${loading ? 'animate-spin' : ''}`} />
          Refresh
        </button>
      </header>

      <main className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {error && (
          <div className="col-span-full bg-red-900/20 border border-red-500/50 p-4 rounded-xl flex items-center gap-3 text-red-200">
            <AlertTriangle className="w-6 h-6" />
            {error}
          </div>
        )}

        {/* A-Index Card */}
        <div className="bg-slate-900 border border-slate-800 p-6 rounded-2xl shadow-xl">
          <div className="flex items-center gap-3 mb-4">
            <Shield className="w-6 h-6 text-blue-400" />
            <h2 className="text-xl font-semibold">A-Index</h2>
          </div>
          {loading ? (
            <div className="animate-pulse space-y-2">
              <div className="h-4 bg-slate-800 rounded w-3/4"></div>
              <div className="h-8 bg-slate-800 rounded w-1/2"></div>
            </div>
          ) : (
            <div>
              <pre className="text-xs text-slate-400 overflow-auto max-h-40 bg-slate-950 p-2 rounded">
                {JSON.stringify(aIndex, null, 2)}
              </pre>
            </div>
          )}
        </div>

        {/* K-Index Card */}
        <div className="bg-slate-900 border border-slate-800 p-6 rounded-2xl shadow-xl">
          <div className="flex items-center gap-3 mb-4">
            <Zap className="w-6 h-6 text-emerald-400" />
            <h2 className="text-xl font-semibold">K-Index</h2>
          </div>
          {loading ? (
            <div className="animate-pulse space-y-2">
              <div className="h-4 bg-slate-800 rounded w-3/4"></div>
              <div className="h-8 bg-slate-800 rounded w-1/2"></div>
            </div>
          ) : (
            <div>
              <pre className="text-xs text-slate-400 overflow-auto max-h-40 bg-slate-950 p-2 rounded">
                {JSON.stringify(kIndex, null, 2)}
              </pre>
            </div>
          )}
        </div>

        {/* Dst-Index Card */}
        <div className="bg-slate-900 border border-slate-800 p-6 rounded-2xl shadow-xl">
          <div className="flex items-center gap-3 mb-4">
            <Sun className="w-6 h-6 text-amber-400" />
            <h2 className="text-xl font-semibold">Dst-Index</h2>
          </div>
          {loading ? (
            <div className="animate-pulse space-y-2">
              <div className="h-4 bg-slate-800 rounded w-3/4"></div>
              <div className="h-8 bg-slate-800 rounded w-1/2"></div>
            </div>
          ) : (
            <div>
              <pre className="text-xs text-slate-400 overflow-auto max-h-40 bg-slate-950 p-2 rounded">
                {JSON.stringify(dstIndex, null, 2)}
              </pre>
            </div>
          )}
        </div>

        {/* Info Box */}
        <div className="col-span-full bg-blue-900/10 border border-blue-500/30 p-6 rounded-2xl flex gap-4">
          <Info className="w-8 h-8 text-blue-400 shrink-0" />
          <div>
            <h3 className="text-lg font-semibold text-blue-200">About Space Weather Data</h3>
            <p className="text-slate-400 mt-1">
              Data is sourced from the Australian Bureau of Meteorology (BOM) Space Weather Services. 
              The indices track geomagnetic disturbances which can affect satellite communications, 
              power grids, and aurora visibility.
            </p>
          </div>
        </div>
      </main>

      <footer className="max-w-6xl mx-auto mt-12 pt-8 border-t border-slate-800 text-center text-slate-500 text-sm">
        &copy; {new Date().getFullYear()} Space Weather Analysis Application
      </footer>
    </div>
  )
}

export default App