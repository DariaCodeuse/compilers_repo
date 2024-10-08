import ply.lex as lex
import json
import copy

# Cargar el JSON
with open('tokens.json') as f:
    data = json.load(f)         # Para hacer tokens
dataTok = copy.deepcopy(data)     # Para agregar variables y cadenas

dataTok["variable"]["a"] = "VARIABLE"
dataTok["variable"]["b"] = "VARIABLE"
dataTok["variable"]["c"] = "VARIABLE"

dataTok["cadena"]["la"] = "CADENA"
dataTok["cadena"]["suma"] = "CADENA"
dataTok["cadena"]["es"] = "CADENA"

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
tokens += ["VARIABLE", "CADENA", "COMILLA"]

# Regular expression rules for simple tokens
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMA= r'\,'
t_SEMICOLON = r';'
t_ADICION = r'\+'
t_IGUAL   = r'='
t_PROGRAMA = r'PROGRAMA'

# A regular expression rule with some action code}
def t_IDENTIFICADOR(t):
    r'Suma'
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
    return t

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


def all_tokens(input):
    # Inicializar el número de línea en 1
    lexer.lineno = 1
    lexer.input(input)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break

        lin = tok.lineno
        tv = tok.value
        pr = "X" if tok.type in reservada.values() else ""
        iD = "X" if tok.type == "IDENTIFICADOR" else ""
        var = "X" if tok.type == "VARIABLE" else ""
        nu = "X" if tok.type == "NUMERO" else ""
        cad = "X" if tok.type == "CADENA" else ""
        sim = "X" if tok.type in data['simbolo'].values() else ""
        
        tipo = "Desconocido"
            # nombre de dict #diccionario
        for categoria, tokens_categoria in dataTok.items():
            print(tokens_categoria)
            if tok.type in tokens_categoria.values():
                tipo = categoria.capitalize()  # Capitaliza el nombre de la categoría
                break

        tokens.append((lin, tv, pr, iD, var, nu, cad, sim, tipo))
    return tokens

### quieres que el data te sirva para identificar a que catagoria pertenece cada token
