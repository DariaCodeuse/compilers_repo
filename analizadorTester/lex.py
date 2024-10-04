import ply.lex as lex

# Lista de tokens
tokens = (
    'IDENTIFIER',
    'INT',
    'FLOAT',
    'CHAR',
    'DOUBLE',
    'SEMICOLON',
    'COMMA',
    'EQUALS',
)

# Definición de expresiones regulares para los tokens
t_INT = r'int'
t_FLOAT = r'float'
t_CHAR = r'char'
t_DOUBLE = r'double'
t_SEMICOLON = r';'
t_COMMA = r','
t_EQUALS = r'='

# Identificador: debe comenzar con una letra o guion bajo y puede tener letras, números o guiones bajos
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Ignorar espacios y saltos de línea
t_ignore = ' \t\n'

def t_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p.value}'")
    else:
        print("Error de sintaxis en la entrada")

# Crear el lexer
lexer = lex.lex()

codigo = """
int a, b, c;
float = x, y;
"""

lexer.input(codigo)
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
