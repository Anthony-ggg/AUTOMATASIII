"""
Definición de tokens para el analizador léxico PLY.
Equivalente a los símbolos definidos en sym.java (generado por CUP).
"""

# Lista de nombres de tokens reconocidos por el lexer
tokens = (
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'LPAREN',
    'RPAREN',
)

# Mapeo de tipo de token a nombre legible (equivalente a TOKEN_NAMES en Java)
TOKEN_DISPLAY_NAMES = {
    'IDENTIFIER':  'IDENTIFICADOR',
    'NUMBER':      'NUMERO',
    'PLUS':        'OPERADOR_SUMA',
    'MINUS':       'OPERADOR_RESTA',
    'TIMES':       'OPERADOR_MULTIPLICACION',
    'DIVIDE':      'OPERADOR_DIVISION',
    'EQUALS':      'OPERADOR_ASIGNACION',
    'LPAREN':      'PARENTESIS_IZQ',
    'RPAREN':      'PARENTESIS_DER',
}
