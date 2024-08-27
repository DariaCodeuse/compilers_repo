# .\.venv\Scripts\activate

import ply.lex as lex
import json
from flask import Flask, render_template, request

# Instancia de App en Flask
app = Flask(__name__)

# Cargar el JSON
with open('tokens.json') as f:
    data = json.load(f)

reserved = data['reserved']
print(reserved)

tokens = list(data.keys())
print(tokens)


# Reglas para los tokens
t_FOR = r"for"
t_DO = r'do'
t_WHILE = r'while'
t_IF = r'if'
t_ELSE = r'else'
t_STATIC = r'static'
t_VOID = r'void"'
t_PUNTO = r'd+.d+\;?'

t_ignore = ' \t\n\r'
t_PABIERTO = r'\('
t_PCERRADO = r'\)'

def t_error(t):
    print('Caracter no valido', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form.get('code', '')
        lexer.input(code)  # Asegúrate de usar 'code' y no 'content'

        result_lexema = [
            (f"Reservada {token.type.capitalize()}" if token.type in reserved.values()
            else "Parentesis de apertura" if token.type == "PABIERTO"
            else "Parentesis de cierre" if token.type == "PCERRADO"
            else f"Token desconocido ({token.type})", token.value)
            for token in lexer
        ]

        return render_template('index.html', tokens=result_lexema)
    return render_template('index.html', tokens=None)

if __name__ == "__main__":
    app.run(debug=True)
