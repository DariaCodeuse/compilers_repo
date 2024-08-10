# Mi primer Analizador lexico que solo reconoce:
# Numeros enteros, identificador, operadores

import re

# 1. Definicion de tokens
tokens = [
    ('NUMERO', r'\d+'),                     # Numero entero
    ('IDENTIFICADOR', r'[A-Z,a-z]\w*'),     # Identificador
    ('SUMA', r'\+'),                        # Operador suma
    ('RESTA', r'-'),                        # Operador rsta
    ('MULTI', r'\*'),                       # Operador multipliacacion
    ('DIVI', r'/'),                         # Operador division
    ('ESPACIO', r'\s+'),                    # Espacios en blanco
    ('IPAREN', r'\('),                      # Parentesis izquierdo
    ('DPAREN', r'\)'),                      # Parentesis derecho
]

# Token expresiones regulares patrones
token-regex = '|'.join(f'(?P<{name}>{pattem})' for name, pattem in tokens)
get_token = re.compile(token_regex).match

# 2. Funcion de analisis lexico
def tokenize(code):
  line_number = 1
  line_start = 0
  position = 0
  tokens = []

while positon < len(code):
    match = get_token(code, position)
    if not match:
      raise RuntimeError(f´Error de Analisis {position}´)
    
    for name, value in match.groupdict().items():
      if value:
        if name != 'ESPACIO':
          tokens.append((name, value))
        break
    position = match.end()

    return tokens

    code = " "
    x = 2 + 4 * (2 - 8)
    " "
    tokens = tokenize(code)
    for token in tokens:
      print(token)
