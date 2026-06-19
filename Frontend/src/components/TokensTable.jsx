function TokensTable({ tokens }) {
  if (!tokens || tokens.length === 0) return null

  const hasDisplay = 'display' in tokens[0]

  return (
    <div>
      <h2>Tokens</h2>
      <div className="tokens-table-wrapper">
        <table className="tokens-table">
          <thead>
            <tr>
              <th>Tipo</th>
              {hasDisplay && <th>Display</th>}
              <th>Lexema</th>
              <th>Línea</th>
              <th>Columna</th>
            </tr>
          </thead>
          <tbody>
            {tokens.map((t, i) => (
              <tr key={i}>
                <td>{t.type}</td>
                {hasDisplay && <td>{t.display}</td>}
                <td>{t.lexeme}</td>
                <td>{t.line}</td>
                <td>{t.column}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default TokensTable
