"""
Punto de entrada del analizador léxico y sintáctico en Python (PLY).
Equivalente funcional a Main.java del proyecto JFlex + CUP.

Uso:
    python main.py                      # Analiza la entrada por defecto
    python main.py examples/entrada.txt # Analiza un archivo de texto
    python main.py --json               # Salida en formato JSON
    python main.py --only-lexer         # Solo análisis léxico (sin parser)
"""

import sys
import json
import os

from lexer.lexer import tokenize
from parser.parser_rules import parse


def print_banner():
    print("=" * 55)
    print("  Analizador Léxico y Sintáctico con PLY")
    print("  APE 11 - Teoría de Autómatas y Computabilidad")
    print("=" * 55)


def print_tokens_table(tokens_list: list[dict]):
    """Imprime los tokens en formato tabular (equivalente a printTokens en Java)."""
    header = f"{'TIPO':<28} {'LEXEMA':<15} {'LÍNEA':<8} {'COLUMNA':<8}"
    print(header)
    print("-" * len(header))
    for tok in tokens_list:
        print(f"{tok['display']:<28} {tok['lexeme']:<15} {tok['line']:<8} {tok['column']:<8}")


def print_tokens_arrows(tokens_list: list[dict]):
    """Imprime los tokens en formato flecha (formato solicitado por la guía)."""
    for tok in tokens_list:
        print(f"{tok['display']} -> {tok['lexeme']}")


def save_output(result: dict, filepath: str):
    """Guarda el resultado completo del análisis en un archivo JSON."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\nResultado guardado en: {filepath}")


def run_lexer(source: str) -> tuple[list[dict], list[str]]:
    """Ejecuta el análisis léxico. Retorna (tokens, errores)."""
    errors = []
    try:
        tokens_list = tokenize(source)
    except SyntaxError as e:
        tokens_list = []
        errors.append(f"Error léxico: {e}")
    return tokens_list, errors


def run_parser(source: str) -> tuple[object, list[str]]:
    """Ejecuta el análisis sintáctico. Retorna (AST, errores)."""
    errors = []
    ast = None
    try:
        ast = parse(source)
    except SyntaxError as e:
        errors.append(f"Error sintáctico: {e}")
    return ast, errors


def main():
    default_input = "x + y = 30\nx - y = 6"

    flags = {'--json', '--only-lexer'}
    use_json = '--json' in sys.argv
    only_lexer = '--only-lexer' in sys.argv
    args = [a for a in sys.argv[1:] if a not in flags]

    if args:
        filepath = args[0]
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                source = f.read().rstrip('\n')
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{filepath}'")
            sys.exit(1)
    else:
        source = default_input

    print_banner()
    print(f"\nEntrada analizada:\n{source}\n")

    # ── Análisis léxico ──────────────────────────────────────
    tokens_list, lex_errors = run_lexer(source)

    print(f"--- Análisis Léxico ({len(tokens_list)} tokens) ---\n")

    if lex_errors:
        for err in lex_errors:
            print(err)
    elif use_json:
        print(json.dumps(tokens_list, ensure_ascii=False, indent=2))
    else:
        print_tokens_arrows(tokens_list)
        print()
        print_tokens_table(tokens_list)

    # ── Análisis sintáctico ──────────────────────────────────
    ast = None
    syn_errors = []

    if not only_lexer and not lex_errors:
        ast, syn_errors = run_parser(source)

        print(f"\n--- Análisis Sintáctico ---\n")

        if syn_errors:
            for err in syn_errors:
                print(err)
        else:
            print(f"Éxito: True")
            print(f"Ecuaciones encontradas: {len(ast)}")
            print(f"\nAST (JSON):")
            print(json.dumps(ast, ensure_ascii=False, indent=2))

    # ── Resultado consolidado ────────────────────────────────
    all_errors = lex_errors + syn_errors
    result = {
        'success': len(all_errors) == 0,
        'message': (
            f"Análisis completado exitosamente. {len(tokens_list)} tokens encontrados."
            if not all_errors
            else all_errors[0]
        ),
        'tokens': tokens_list,
        'parsedResult': ast,
    }

    save_output(result, 'output/resultado.json')


if __name__ == '__main__':
    main()
