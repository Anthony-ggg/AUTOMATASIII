# Analizador Léxico y Sintáctico con PLY (Python Lex-Yacc)

**APE 11** — Teoría de Autómatas y Computabilidad Avanzada  
Universidad Nacional de Loja — FEIRNNR — Carrera de Computación

## Descripción

Implementación de un analizador léxico y sintáctico utilizando **PLY (Python Lex-Yacc)**,
equivalente funcional al proyecto Java con JFlex + CUP.

- **Lexer (ply.lex):** reconoce identificadores, números enteros, operadores aritméticos
  (`+`, `-`, `*`, `/`), operador de asignación (`=`) y paréntesis.
- **Parser (ply.yacc):** construye un AST (árbol de sintaxis abstracta) a partir de
  ecuaciones con la misma gramática y estructura JSON que produce `Parser.cup`.

## Requisitos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)

## Instalación

```bash
# 1. Verificar la versión de Python
python --version   # Debe ser 3.10+

# 2. Instalar dependencias
pip install -r requirements.txt
```

## Ejecución

```bash
# Análisis léxico + sintáctico con entrada por defecto
python main.py

# Analizar un archivo de entrada
python main.py examples/entrada.txt

# Salida en formato JSON
python main.py --json

# Solo análisis léxico (sin parser)
python main.py --only-lexer

# Combinar opciones
python main.py examples/entrada.txt --json
```

## Estructura del proyecto

```
Python/
├── lexer/
│   ├── __init__.py          # Exportaciones del módulo lexer
│   ├── tokens.py            # Definición de tokens (equivalente a sym.java)
│   └── lexer.py             # Analizador léxico PLY (equivalente a Lexer.jflex)
├── parser/
│   ├── __init__.py          # Exportaciones del módulo parser
│   └── parser_rules.py     # Gramática PLY yacc (equivalente a Parser.cup)
├── examples/
│   └── entrada.txt          # Archivo de prueba con ecuaciones
├── output/                  # Directorio de salida (generado automáticamente)
├── main.py                  # Punto de entrada (equivalente a Main.java)
├── requirements.txt         # Dependencias del proyecto
├── .gitignore
└── README.md
```

## Equivalencia Java ↔ Python

| Componente          | Java (JFlex + CUP)                  | Python (PLY)                |
|---------------------|--------------------------------------|-----------------------------|
| Lexer               | `Lexer.jflex`                        | `lexer/lexer.py`            |
| Símbolos/Tokens     | `sym.java` (generado por CUP)       | `lexer/tokens.py`           |
| Parser              | `Parser.cup`                         | `parser/parser_rules.py`    |
| Servicio de análisis| `LexicalAnalyzerService.java`        | `tokenize()` + `parse()`    |
| Punto de entrada    | `Main.java`                          | `main.py`                   |
| Modelo de token     | `TokenDTO.java`                      | `dict` con mismas claves    |
| Resultado           | `ParseResponse.java`                 | `dict` JSON equivalente     |

## Funcionamiento

1. **tokens.py** define la lista de tokens reconocidos, equivalentes a los terminales
   de `Parser.cup`.

2. **lexer.py** implementa las reglas léxicas con las mismas expresiones regulares
   que `Lexer.jflex`. Cada token incluye tipo, lexema, línea y columna.

3. **parser_rules.py** define la gramática con `ply.yacc`, traducción directa de
   `Parser.cup`. Produce un AST idéntico en estructura: lista de ecuaciones, cada una
   con sub-árboles `left`/`right` de nodos `binary`, `identifier` y `number`.

4. **main.py** orquesta ambos análisis e imprime los resultados.

## Ejemplo de salida

```
Entrada analizada:
x + y = 30
x - y = 6

--- Análisis Léxico (10 tokens) ---

IDENTIFICADOR -> x
OPERADOR_SUMA -> +
IDENTIFICADOR -> y
OPERADOR_ASIGNACION -> =
NUMERO -> 30
IDENTIFICADOR -> x
OPERADOR_RESTA -> -
IDENTIFICADOR -> y
OPERADOR_ASIGNACION -> =
NUMERO -> 6

--- Análisis Sintáctico ---

Éxito: True
Ecuaciones encontradas: 2

AST (JSON):
[
  {
    "left": {
      "type": "binary",
      "operator": "+",
      "left": { "type": "identifier", "value": "x" },
      "right": { "type": "identifier", "value": "y" }
    },
    "right": { "type": "number", "value": 30 }
  },
  {
    "left": {
      "type": "binary",
      "operator": "-",
      "left": { "type": "identifier", "value": "x" },
      "right": { "type": "identifier", "value": "y" }
    },
    "right": { "type": "number", "value": 6 }
  }
]
```

## Tokens reconocidos

| Token PLY     | Nombre legible             | Expresión regular         |
|---------------|----------------------------|---------------------------|
| IDENTIFIER    | IDENTIFICADOR              | `[a-zA-Z_][a-zA-Z0-9_]*` |
| NUMBER        | NUMERO                     | `[0-9]+`                  |
| PLUS          | OPERADOR_SUMA              | `\+`                      |
| MINUS         | OPERADOR_RESTA             | `-`                       |
| TIMES         | OPERADOR_MULTIPLICACION    | `\*`                      |
| DIVIDE        | OPERADOR_DIVISION          | `/`                       |
| EQUALS        | OPERADOR_ASIGNACION        | `=`                       |
| LPAREN        | PARENTESIS_IZQ             | `\(`                      |
| RPAREN        | PARENTESIS_DER             | `\)`                      |

## Gramática

```
program         → equation_list
equation_list   → equation | equation_list equation
equation        → expression '=' expression
expression      → expression ('+' | '-' | '*' | '/') expression | term
term            → IDENTIFIER | NUMBER | '(' expression ')'
```
