from flask import Flask, render_template,request
from flask_cors import CORS
from lex import all_tokens
from syntax import parser_for_statement

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    tokens = []
    syntax_errors = []
    
    if request.method == 'POST':
        code = request.form.get('code', '')

        if code.strip():
            try:                
                tokens = all_tokens(code)       # Análisis léxico
                parser_for_statement(code)      # Análisis sintáctico
                syntax_errors = parser_for_statement(code)
            except Exception as e:
                # En caso de un error crítico (no previsto), lo agregamos a la lista de errores
                syntax_errors.append(f"Error crítico al analizar el código: {str(e)}")

    # Renderizar la página con los resultados
    return render_template(
        'index.html',
        tokens=tokens,
        errors=syntax_errors
    )

if __name__ == '__main__':
    app.run(debug=True)
