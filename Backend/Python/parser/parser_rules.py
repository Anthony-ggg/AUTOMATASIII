"""
Analizador sintáctico implementado con PLY (yacc).
Traducción directa de la gramática definida en Parser.cup (Java/CUP).

Gramática:
    program         → equation_list
    equation_list   → equation | equation_list equation
    equation        → expression EQUALS expression
    expression      → expression (PLUS|MINUS|TIMES|DIVIDE) expression | term
    term            → IDENTIFIER | NUMBER | LPAREN expression RPAREN

Produce un AST (árbol de sintaxis abstracta) como diccionarios anidados,
con la misma estructura JSON que genera el parser Java.
"""

import ply.yacc as yacc
from lexer.tokens import tokens  # noqa: F401 — requerido por PLY

# ── Precedencia (idéntica a Parser.cup) ──────────────────────────

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# ── Reglas gramaticales ──────────────────────────────────────────

def p_program(p):
    '''program : equation_list'''
    p[0] = p[1]


def p_equation_list_single(p):
    '''equation_list : equation'''
    p[0] = [p[1]]


def p_equation_list_multiple(p):
    '''equation_list : equation_list equation'''
    p[1].append(p[2])
    p[0] = p[1]


def p_equation(p):
    '''equation : expression EQUALS expression'''
    p[0] = {
        'left': p[1],
        'right': p[3],
    }


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = {
        'type': 'binary',
        'operator': p[2],
        'left': p[1],
        'right': p[3],
    }


def p_expression_term(p):
    '''expression : term'''
    p[0] = p[1]


def p_term_identifier(p):
    '''term : IDENTIFIER'''
    p[0] = {
        'type': 'identifier',
        'value': p[1],
    }


def p_term_number(p):
    '''term : NUMBER'''
    p[0] = {
        'type': 'number',
        'value': p[1],
    }


def p_term_paren(p):
    '''term : LPAREN expression RPAREN'''
    p[0] = p[2]


# ── Manejo de errores sintácticos ────────────────────────────────

def p_error(p):
    if p:
        raise SyntaxError(
            f"Error sintáctico: token inesperado '{p.value}' "
            f"(tipo {p.type}) en línea {p.lineno}"
        )
    raise SyntaxError("Error sintáctico: fin de entrada inesperado")


# ── Construcción del parser ──────────────────────────────────────

def build_parser(**kwargs) -> yacc.LRParser:
    """Construye y retorna una instancia del parser."""
    return yacc.yacc(debug=False, write_tables=False, **kwargs)


def parse(source: str) -> list[dict]:
    """
    Analiza sintácticamente el texto de entrada y retorna el AST.

    Retorna una lista de ecuaciones, donde cada ecuación es un diccionario
    con claves 'left' y 'right' que contienen los sub-árboles de expresiones.

    Estructura idéntica a la producida por Parser.cup en Java.
    """
    from lexer.lexer import build_lexer
    lexer = build_lexer()
    parser_instance = build_parser()
    return parser_instance.parse(source, lexer=lexer)
