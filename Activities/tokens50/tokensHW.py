# Realiza un analizador Léxico en python 50 tokens

import re

# 1. Definicion de tokens
token_patterns = [
    ('NUMERO', r'\d+'),                      # Número entero
    ('SUMA', r'\+'),                         # Operador de suma
    ('RESTA', r'-'),                         # Operador de resta
    ('MULTIPLICACION', r'\*'),               # Operador de multiplicación
    ('DIVISION', r'/'),                      # Operador de división
    ('PARENTESIS_IZQ', r'\('),               # Paréntesis izquierdo
    ('PARENTESIS_DER', r'\)'),               # Paréntesis derecho
    ('ESPACIO', r'\s+'),                     # Espacios
    ('IGUAL', r'\='),
    ('PRINT', r'print'),
    
    ('IDENTIFICADOR', r'[a-zA-Z_][a-zA-Z_0-9]*'),  # Identificadores
    ('PUNTO', r'\.'),                             # Punto
    ('COMA', r','),                               # Coma
    ('PUNTO_Y_COMA', r';'),                       # Punto y coma
    ('DOS_PUNTOS', r':'),                         # Dos puntos
    ('COMILLAS_DOBLES', r'\"'),                   # Comillas dobles
    ('COMILLAS_SIMLES', r'\''),                   # Comillas simples
    ('CORCHETE_IZQ', r'\['),                      # Corchete izquierdo
    ('CORCHETE_DER', r'\]'),                      # Corchete derecho
    ('LLAVE_IZQ', r'\{'),                         # Llave izquierda
    ('LLAVE_DER', r'\}'),                         # Llave derecha
    ('MENOR', r'<'),                              # Operador menor que
    ('MAYOR', r'>'),                              # Operador mayor que
    ('MENOR_IGUAL', r'<='),                       # Menor o igual que
    ('MAYOR_IGUAL', r'>='),                       # Mayor o igual que
    ('DIFERENTE', r'!='),                         # Diferente
    ('INCREMENTO', r'\+\+'),                      # Incremento
    ('DECREMENTO', r'--'),                        # Decremento
    ('AND', r'&&'),                               # Operador AND
    ('OR', r'\|\|'),                              # Operador OR
    ('NOT', r'!'),                                # Operador NOT
    ('MODULO', r'%'),                             # Operador módulo
    ('ASIGNACION_SUMA', r'\+='),                  # Asignación con suma
    ('ASIGNACION_RESTA', r'-='),                  # Asignación con resta
    ('ASIGNACION_MULTIPLICACION', r'\*='),        # Asignación con multiplicación
    ('ASIGNACION_DIVISION', r'/='),               # Asignación con división
    ('ASIGNACION_MODULO', r'%='),                 # Asignación con módulo
    ('CONDICIONAL_IF', r'\bif\b'),                # Palabra clave if
    ('CONDICIONAL_ELSE', r'\belse\b'),            # Palabra clave else
    ('CICLO_FOR', r'\bfor\b'),                    # Palabra clave for
    ('CICLO_WHILE', r'\bwhile\b'),                # Palabra clave while
    ('CICLO_DO', r'\bdo\b'),                      # Palabra clave do
    ('SWITCH', r'\bswitch\b'),                    # Palabra clave switch
    ('CASE', r'\bcase\b'),                        # Palabra clave case
    ('BREAK', r'\bbreak\b'),                      # Palabra clave break
    ('CONTINUE', r'\bcontinue\b'),                # Palabra clave continue
    ('RETURN', r'\breturn\b'),                    # Palabra clave return
    ('FUNCTION', r'\bfunction\b'),                # Palabra clave function
    ('CLASS', r'\bclass\b'),                      # Palabra clave class
    ('CONSTRUCTOR', r'\bconstructor\b'),          # Palabra clave constructor
    ('NUEVO_OBJETO', r'\bnew\b'),                 # Palabra clave new
    ('THIS', r'\bthis\b'),                        # Palabra clave this
    ('STATIC', r'\bstatic\b'),                    # Palabra clave static
    ('VOID', r'\bvoid\b'),                        # Palabra clave void
    ('NULL', r'\bnull\b'),                        # Valor null
    ('BOOLEANO', r'\btrue\b|\bfalse\b'),          # Booleanos true/false
]

# Token expresiones regulares patrones
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_patterns)
get_token = re.compile(token_regex).match

# 2. Funcion de analisis lexico
def tokenize(code):
  line_number = 1
  line_start = 0
  position = 0
  tokens = []

  while position < len(code):
    match = get_token(code, position)
    if not match:
      raise RuntimeError(f'Error de Analisis en posicion {position}')
        
    for name, value in match.groupdict().items():
      if value:
        if name != 'ESPACIO':
          tokens.append((name, value))
        break
    position = match.end()

  return tokens  # Mover el return fuera del bucle while

code = "x = 2 + 4 * (2 - 8) = 8 , if (z > 0)function suma(a, b) else if (z < 0)"
tokens = tokenize(code)

for i, token in enumerate(tokens, start=1):
    print(f"{i}. {token}")