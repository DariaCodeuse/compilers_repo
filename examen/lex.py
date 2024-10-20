import ply.lex as lex
import json
import copy

# Cargar el JSON
with open('tokens.json') as f:
    data = json.load(f)         # Para hacer tokens
dataTok = copy.deepcopy(data)     # Para agregar variables y cadenas


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
tokens += ["CADENA", "COMENTARIO"]

print(tokens)
# Regular expression rules for simple tokens
t_USING      = r'using'
t_NAMESPACE  = r'namespace'
t_CLASS      = r'class'
t_STATIC     = r'static'
t_VOID       = r'void'
t_STRING     = r'string'
t_SYSTEM     = r'System'
t_HELLOWORLD = r'HelloWorld'
t_HELLO      = r'Hello'
t_MAIN       = r'Main'
t_ARGS       = r'args'
t_CONSOLE    = r'Console'
t_WRITELINE  = r'WriteLine'

# Delimitadores
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACE     = r'\{'
t_RBRACE     = r'\}'
t_SEMICOLON  = r';'
t_PUNTO  = r'.'
t_LBRACKET   = r'\['
t_RBRACKET   = r'\]'

# A regular expression rule with some action code}

# Track line numbers
def t_CADENA(t):
    r'"[^"]*"'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
t_ignore  = ' \t'

def t_COMENTARIO(t):
    r'//.*'
    pass

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# SOLO PARA TESTEO
data = '''
using System;

namespace HelloWorld
{
    class Hello {
        static void Main(string[] args)
        {   // prints hello world
            System.Console.WriteLine("Hello World!");
        }
    }
}
'''
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)


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
        nu = "X" if tok.type == "NUMERO" else ""
        cad = "X" if tok.type == "CADENA" else ""
        sim = "X" if tok.type in data['simbolo'].values() else ""
        
        tipo = "Desconocido"
            # nombre de dict #diccionario
        for categoria, tokens_categoria in dataTok.items():
            if tok.type in tokens_categoria.values():
                tipo = categoria.capitalize()  # Capitaliza el nombre de la categoría
                break

        tokens.append((lin, tv, pr, iD, nu, cad, sim, tipo))
    return tokens

### quieres que el data te sirva para identificar a que catagoria pertenece cada token
