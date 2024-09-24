from flask import Flask, render_template, request
import ply.yacc as yacc
from lex import tokens 

app = Flask(__name__)

# Definición del parser (Yacc)
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_error(p):
    print(f"Syntax error at '{p.value}'" if p else "Syntax error at EOF")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code']
        
        # Construir el parser
        parser = yacc.yacc()
        
        # Análisis léxico
        tokens_list = analyze_code(code)
        
        # Análisis sintáctico
        parse_result = parser.parse(code)
        
        # Renderizar resultados
        return render_template('index.html', tokens=tokens_list, parse=parse_result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
