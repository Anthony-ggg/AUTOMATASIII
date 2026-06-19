import { useState } from 'react'
import TokensTable from './TokensTable'
import AstViewer from './AstViewer'

function PythonAnalyzer() {
  const [input, setInput] = useState('x + y = 30\nx - y = 6')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const analyze = async () => {
    setLoading(true)
    setError(null)
    setResult(null)
    try {
      const res = await fetch('/api/python/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ input }),
      })
      const data = await res.json()
      if (!res.ok) throw new Error(data.error || 'Error desconocido')
      setResult(data)
    } catch (e) {
      setError(e.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <div className="input-section">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ingrese las ecuaciones a analizar..."
        />
        <button className="btn-analyze" onClick={analyze} disabled={loading}>
          {loading ? 'Analizando...' : 'Analizar'}
        </button>
      </div>

      {loading && <p className="loading">Ejecutando análisis léxico y sintáctico...</p>}

      {error && <p className="error-message">Error: {error}</p>}

      {result && (
        <div className="result-section">
          <div className="status-bar">
            <span className={`success-badge ${result.success ? 'ok' : 'error'}`}>
              {result.success ? 'Éxito' : 'Error'}
            </span>
            <span className="message">{result.message}</span>
          </div>

          <TokensTable tokens={result.tokens} />
          <AstViewer parsedResult={result.parsedResult} />
        </div>
      )}
    </div>
  )
}

export default PythonAnalyzer
