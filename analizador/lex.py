import ply.lex as lex

# Definición de tokens
tokens = ['NUMERO', 'SUMA', 'MENOS', 'SLASH_IZQ', 'DIVIDE', 'LPAREN', 'RPAREN']

# Reglas de expresión regular para tokens simples
t_SUMA = r'\+'
t_RESTA = r'-'
t_SLASH_IZQ = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore = ' \t'

# Regla para reconocer números
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)  # Convierte a número
    return t

# Regla para manejar errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

# Función para analizar el código
def analyze_code(code):
    lexer.input(code)
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append((tok.type, tok.value, tok.lineno))
    return tokens_list
