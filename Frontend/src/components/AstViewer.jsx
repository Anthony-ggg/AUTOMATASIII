function AstViewer({ parsedResult }) {
  if (!parsedResult) return null

  return (
    <div>
      <h2>AST (Árbol de Sintaxis Abstracta)</h2>
      <pre className="ast-json">
        {JSON.stringify(parsedResult, null, 2)}
      </pre>
    </div>
  )
}

export default AstViewer
