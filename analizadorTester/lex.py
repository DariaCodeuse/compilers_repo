import ply.lex as lex
import json

# Cargar el JSON
with open('tokens.json') as f:
    data = json.load(f)
reserved = data["reserved"]

# List of token names (Always required)
tokens = [token for category in data.values() for token in category.values()]
tokens += ["IDENTIFIER", "STRING", "NUMBER"]


# Regular expression rules for simple tokens
t_EQUALS   = r'='
t_PLUS    = r'\+'
t_LESS_EQUAL   = r'<='
t_INCREMENT  = r'\+\+'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_DOT = r'\.'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
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

# Test it out
data = '''
for (int i = 1; i <= 5; i++) {
    System.out.println ("El valor de la cifra es: " + i);
}
'''

# Tokenize
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

all_tokens(data)
