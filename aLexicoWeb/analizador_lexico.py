import ply.yacc as yacc
import json
from flask import Flask, render_template, request

# Instancia de App en Flask
app = Flask(__name__)

# Cargar el JSON
with open('tokens.json') as f:
    data = json.load(f)

# Cargar lista de tokens
tokens = [token for category in data.values() for token in category.values()]
tokens.append("NUMERO")
print(tokens)

# Cargar solo NOMBRES DE TOKENS (Claves)
typeTokens = list(data.keys())
typeTokens.append("number")
print(typeTokens)

# Reglas para los tokens
t_FOR = r"for"
t_DO = r'do'
t_WHILE = r'while'
t_IF = r'if'
t_ELSE = r'else'
t_PUBLIC = r'public'
t_STATIC = r'static'
t_INT = r'int'
t_VOID = r'void'

t_P_ABIERTO = r'\('
t_P_CERRADO = r'\)'
t_LLAVE_ABIERTA = r'\{'
t_LLAVE_CERRADA = r'\}'  # Este nombre tenía un error, lo corregí
t_CORCHETE_I = r'\['
t_CORCHETE_D = r'\]'

t_VAR = r'var'
t_LET = r'let'
t_CONST = r'const'
t_FUNCTION = r'function'
t_MAIN = r'main'

t_IGUAL = r'='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION_S = r'/'
t_DIVISION_E = r'//'

t_PUNTO = r'\.'  # Es necesario escapar el punto
t_PUNTO_Y_COMA = r';'
t_COMA = r','

t_NUMERO = r'\d+'

t_ignore = ' \t'

# Regla para contar los números de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print('Caracter no válido', t.value[0])
    t.lexer.skip(1)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form.get('code', '')
        lexer = lex.lex()
        lexer.input(code)
        
        result_lexema = []
        for token in lexer:
            descripcion = "Desconocido"
            
            # Convertir el valor del token a minúsculas para buscar en el JSON
            token_value = token.value.lower()
            
            # Buscar la descripción del token
            for category, tokens_dict in data.items():
                if token_value in tokens_dict:
                    descripcion = category
                    break
            
            result_lexema.append((descripcion.upper()          , token.value, token.lineno))
        
        return render_template('index.html', tokens=result_lexema)
    return render_template('index.html', tokens=None)

if __name__ == "__main__":
    app.run(debug=True)
