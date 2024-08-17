import ply.lex as lex
from flask import Flask, render_template, request

app = Flask(_name_)

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

@app.router('/', metodos=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form.get('code', '')
        # lexer.input(content)

        result_lexema = [
            (f"Reservada {token.type.capitalize()}" if token.type in reserved.values(
            ) else "Parentesis de apertura" if token.type == "ABIERTO" else "Parentesis de cierre", token.value)
            for token in lexer
        ]
        return render_template('Home.html', tokens=result_lexema)
    return render_template('Home.html', tokens=None)


if _name_ == "_main_":
    app.run(debug=True)
