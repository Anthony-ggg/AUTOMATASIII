import { useState } from 'react'
import PythonAnalyzer from './components/PythonAnalyzer'
import JavaAnalyzer from './components/JavaAnalyzer'
import './App.css'

function App() {
  const [activeTab, setActiveTab] = useState('python')

  return (
    <div className="app">
      <header className="header">
        <h1>Analizador Léxico y Sintáctico</h1>
        <p className="subtitle">APE 11 - Teoría de Autómatas y Computabilidad</p>
      </header>

      <nav className="tabs">
        <button
          className={`tab ${activeTab === 'python' ? 'active' : ''}`}
          onClick={() => setActiveTab('python')}
        >
          Analizador Python
        </button>
        <button
          className={`tab ${activeTab === 'java' ? 'active' : ''}`}
          onClick={() => setActiveTab('java')}
        >
          Analizador Java
        </button>
      </nav>

      <main className="content">
        {activeTab === 'python' ? <PythonAnalyzer /> : <JavaAnalyzer />}
      </main>
    </div>
  )
}

export default App
