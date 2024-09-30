import ply.lex as lex

keyWords = {
    "reserved": {
        "for": "FOR",  #
        "int": "INT",  #
        "do": "DO",
        "while": "WHILE",
        "if": "IF",
        "else": "ELSE",
        "public": "PUBLIC",
        "static": "STATIC",
        "void": "VOID",
    },

    "identifier": {
        "System": 'SYSTEM',  # Agregado System
        'out': 'OUT',
        'println': 'PRINTLN',
        "i" : "I"
    },

    "delimiter": {
        "(": "PARENTESIS_L",  #
        ")": "PARENTESIS_R",  #
        "{": "LLAVE_L",  #
        "}": "LLAVE_R",  #
    },

    "operator": {
        "=": "IGUAL",  #
        "+": "SUMA",  #
        "-": "RESTA",
        "*": "MULTI",
        "/": "DIVI",
        "==": "IGUALDAD",
        "<": "MENORQUE",
        ">": "MAYORQUE",
        "<=": "MENORIGUAL",  #
        ">=": "MAYORIGUAL",
        "!": "NEGACION",
        "%": "MODULO",
        "++": "INCREMENTO",  #
    },

    "simbol": {
        ".": 'PUNTO',
        ",": 'COMA',
        ";": 'PUNTO_COMA',
        '"': 'COMILLA_DOBLE'
    }
}

# Tokens ("categorías" que el analizador léxico reconocerá)
tokens = [token for category in keyWords.values() for token in category.values()] + ["NUMERO", "VARIABLE", "CADENA"]
print(tokens)  # prueba

t_ignore = ' \t\r'

# REGLAS para tokens
t_FOR = r'\bfor\b'
t_INT = r'\bint\b'
t_DO = r'\bdo\b'
t_WHILE = r'\bwhile\b'
t_IF = r'\bif\b'
t_ELSE = r'\belse\b'
t_PUBLIC = r'\bpublic\b'
t_STATIC = r'\bstatic\b'
t_VOID = r'\bvoid\b'

t_SYSTEM = r'\bSystem\b'
t_OUT = r'\bout\b'
t_PRINTLN = r'\bprintln\b'
t_I = r'\I'

# Delimitadores
t_PARENTESIS_L = r'\('
t_PARENTESIS_R = r'\)'
t_LLAVE_L = r'\{'
t_LLAVE_R = r'\}'

# Operadores
t_IGUAL = r'='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTI = r'\*'
t_DIVI = r'/'
t_IGUALDAD = r'=='
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_NEGACION = r'!'
t_MODULO = r'%'
t_INCREMENTO = r'\+\+'

# Símbolos
t_PUNTO = r'\.'
t_COMA = r','
t_PUNTO_COMA = r';'
t_COMILLA_DOBLE = r'"'

t_NUMERO = r'\d+'

t_CADENA = 

reserved = keyWords["reserved"]

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')  # Cambiado a 'VARIABLE'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Error de análisis: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
