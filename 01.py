# Mi primer Analizador lexico que solo reconoce:
# Numeros enteros, identificador, operadores

import re

# 1. Definicion de tokens
tokens = [
    ('NUMERO', r´\d+´),                     # Numero entero
    ('IDENTIFICADOR', r´[A-Z,a-z]\w*´),     # Identificador
    ('SUMA', r´\+´),                        # Operador
]


