from lex import crear_lexer
from syntax import crear_parser, errores
from flask import Flask, render_template, request, url_for, redirect
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form.get('code')
        valor = 1

        lexer = crear_lexer()
        parser = crear_parser()

        errores.clear()

        lexer.input(code)
        result_lexema = []

        for tok in lexer:
            if tok.type == 'PABIERTO':
                descripcion = "Paréntesis izquierdo"
            elif tok.type == 'PCERRADO':
                descripcion = "Paréntesis derecho"
            elif tok.type == 'SUMA':
                descripcion = "Signo suma"
            elif tok.type == 'RESTA':
                descripcion = "Signo resta"
            elif tok.type == 'MULTI':
                descripcion = "Signo multiplicación"
            elif tok.type == 'DIVI':
                descripcion = "Signo división"
            elif tok.type == 'NUMERO':
                descripcion = "Número"
            else:
                descripcion = "Decimal"
                
            result_lexema.append((tok.value, descripcion))

        try:
            resultado = parser.parse(code, lexer=lexer)
            if resultado % 1 == 0:
                resultado = int(resultado)
        except Exception as e:
            if not resultado:
                pass
            else:
                resultado = errores[0]
                valor = 0

        return render_template('index.html', valor=valor, resultado=resultado, tokens=result_lexema)

    return render_template('index.html', valor=0, resultado='')

if __name__ == "__main__":
    app.run(debug=True)
