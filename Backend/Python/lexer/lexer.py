"""
Analizador léxico implementado con PLY (Python Lex-Yacc).
Equivalente funcional al Lexer.jflex del proyecto Java.

Reconoce: identificadores, números enteros, operadores aritméticos,
operador de asignación y paréntesis.
"""

import ply.lex as lex
from lexer.tokens import tokens, TOKEN_DISPLAY_NAMES


# --- Reglas de tokens simples (operadores y delimitadores) ---

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'


# --- Reglas de tokens con acción (funciones) ---

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t


def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


# --- Caracteres ignorados ---

t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# --- Manejo de errores ---

def t_error(t):
    raise SyntaxError(
        f"Carácter ilegal '{t.value[0]}' en línea {t.lineno}, "
        f"columna {_find_column(t.lexer.lexdata, t)}"
    )


# --- Utilidades ---

def _find_column(input_text: str, token) -> int:
    """Calcula la columna del token (equivalente a yycolumn + 1 en JFlex)."""
    last_newline = input_text.rfind('\n', 0, token.lexpos)
    return (token.lexpos - last_newline)


def build_lexer() -> lex.Lexer:
    """Construye y retorna una instancia del lexer."""
    return lex.lex()


def tokenize(source: str) -> list[dict]:
    """
    Analiza léxicamente el texto de entrada y retorna una lista de tokens.

    Cada token es un diccionario con las claves:
        - type:       tipo interno del token (e.g. 'IDENTIFIER')
        - display:    nombre legible en español (e.g. 'IDENTIFICADOR')
        - lexeme:     valor textual original
        - line:       número de línea (1-indexed)
        - column:     número de columna (1-indexed)

    Equivalente a LexicalAnalyzerService.getTokens() en Java.
    """
    lexer = build_lexer()
    lexer.input(source)

    result = []
    for tok in lexer:
        column = _find_column(source, tok)
        result.append({
            'type':    tok.type,
            'display': TOKEN_DISPLAY_NAMES.get(tok.type, tok.type),
            'lexeme':  str(tok.value),
            'line':    tok.lineno,
            'column':  column,
        })

    return result
