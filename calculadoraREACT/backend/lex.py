import ply.lex as lex

data_tok = {
  'Paréntesis Izquierdo': 'LPAREN',
  'Paréntesis Derecho': 'RPAREN',
  'Operador Suma': 'ADICION',
  'Operador Resta': 'RESTA',
  'Operador Multiplicación': 'MULTI',
  'Operador División': 'DIVI',
  'Número Entero': 'NUMBER',
  'Punto': "DOT",
  'Igual': 'EQUAL'
}

tokens = list(data_tok.values())
tipo   = list(data_tok.keys())

print(tokens)

# Regular expression rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ADICION = r'\+'
t_RESTA = r'-'
t_MULTI = r'\*'
t_DIVI = r'/'
t_DOT = r'\.'
t_EQUAL = r'='

# Definir una regla para reconocer números enteros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    # Convierte el número a tipo entero
    return t

# Caracteres ignorados (espacios en blanco)
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Caracter no válido: {t.value[0]}")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Función para generar la lista de tokens con descripción
def all_tokens(input_expr):
    lexer.input(input_expr)
    tokens_list = []
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        
        # Obtener la descripción del token (categoría)
        tipo_token = "Desconocido"
        for desc, code in data_tok.items():
            if tok.type == code:
                tipo_token = desc
                break
        
        # Añadir a la lista de tokens: (Token, Descripción)
        tokens_list.append((tok.value, tipo_token))
    
    return tokens_list

# Ejemplo de uso
expression = "(3 + 4) * 5 ="
tokens_with_description = all_tokens(expression)
print(tokens_with_description)
