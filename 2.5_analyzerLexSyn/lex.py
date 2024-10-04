import ply.lex as lex
import json

# Cargar el JSON
with open('tokens.json') as f:
    data = json.load(f)

reservada = data["reservada"]
identificador = data["identificador"]

# List of token names (Always required)
tokens = [token for category in data.values() for token in category.values()]
tokens += ["IDENTIFICADOR", "VARIABLE", "NUMERO", "CADENA"]

variable = []

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
def t_CADENA(t):
    r'"[^"]*"'
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value not in reservada and t.value not in identificador:
        t.type = 'VARIABLE'  # Marca como variable
        identificador[t.value] = t.value  # Registra la nueva variable
    else:
        t.type = reservada.get(t.value, 'IDENTIFICADOR')
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservada.get(t.value, 'IDENTIFICADOR')
    return t

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

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

lexer.input(data)
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
