# .\.venv\Scripts\activate
# afbff5

import ply.lex as lex
from flask import Flask, render_template, request

# Instancia de App en Flask
app = Flask(__name__)

reserved = {
    'for': 'FOR',
    'while': 'WHILE'
}

tokens = ['PABIERTO', 'PCERRADO'] + list(reserved.values())

t_FOR = r'for'
t_WHILE = r'while'
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
             else "Parentesis de cierre", token.value)
            for token in lexer
        ]
        return render_template('index.html', tokens=result_lexema)
    return render_template('index.html', tokens=None)

if __name__ == "__main__":
    app.run(debug=True)
