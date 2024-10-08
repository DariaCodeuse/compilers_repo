import ply.lex as lex
import json

# Cargar el JSON
with open('tokens.json') as f:
    data = json.load(f)         # Para hacer tokens
    dataTok = json.load(f)      # Para agregar variables y cadenas

# Inicializar una lista de categorías (los diccionarios dentro de data)
lista_categorias = []
for nombre_diccionario in data:
    lista_categorias.append(nombre_diccionario)

# Inicializar el diccionario de conteo para cada categoría
token_count = {categoria: [] for categoria in lista_categorias}
reservada = data["reservada"]
identificador = data["identificador"]

# List of token names (Always required)
tokens = [token for category in data.values() for token in category.values()]
tokens += ["IDENTIFICADOR", "VARIABLE", "CADENA", "RESERVADA", "COMILLA"]

# Regular expression rules for simple tokens
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMA= r'\,'
t_SEMICOLON = r';'
t_ADICION = r'\+'
t_IGUAL   = r'='

# A regular expression rule with some action code
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservada.get(t.value, 'IDENTIFICADOR')
    return t

# Identificadores
def t_VARIABLE(t):
    r'\w+'
    if t.value in reservada.keys():
        t.type = reservada[t.value]
    elif len(t.value) > 1:
        t.type = 'CADENA'
    else:
        t.type = 'VARIABLE'
    r'\w+'
    if t.value in reservada.keys():
        t.type = reservada[t.value]
    elif len(t.value) > 1:
        t.type = 'CADENA'
    else:
        t.type = 'VARIABLE'
    return t

# def t_VARIABLE(t):
#     r'[a-zA-Z_][a-zA-Z0-9_]*'
#     if t.value not in reservada and t.value not in identificador:
#         t.type = 'VARIABLE'  # Marca como variable
#         identificador[t.value] = t.value  # Registra la nueva variable
#     else:
#         t.type = reservada.get(t.value, 'IDENTIFICADOR')
#     return t

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
t_ignore  = ' \t'

def t_COMILLA_ignore(t):
    r'"'
    pass

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# SOLO PARA TESTEO
data = '''
programa suma(){
    int a,b,c;
    read a;
    read b;
    c = a+b;
    print("la suma es")
    end;
}
'''

# lexer.input(data)
# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break      # No more input
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)

def all_tokens(input):
    # Inicializar el número de línea en 1
    lexer.lineno = 1
    lexer.input(input)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append((tok.type, tok.value, tok.lineno))
    return tokens