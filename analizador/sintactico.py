import ply.yacc as yacc
from lexico import tokens
from flask import Flask, render_template, request

# Instancia de App en Flask
app = Flask(__name__)

def p_ciclofor(p):
    '''ciclofor : FOR PARENTESIS_L inicializacion PUNTO_COMA condicion PUNTO_COMA incremento PARENTESIS_R cuerpo'''

def p_inicializacion(p):
    '''inicializacion : INT I IGUAL NUMERO'''

def p_condicion(p):
    '''condicion : I MENORIGUAL NUMERO'''

def p_incremento(p):
    '''incremento : I INCREMENTO'''

def p_cuerpo(p):
    '''cuerpo : LLAVE_L sentencia LLAVE_R'''

def p_sentencia(p):
    '''sentencia : SYSTEM PUNTO OUT PUNTO PRINTLN PARENTESIS_L cadena SUMNA I PARENTESIS_R PUNTO_COMA'''

def p_cadena(p):
    '''cadena : CADENA'''

@app.route('/', methods = ['GET','POST'])
def index():
    global errores
    errores = []
    color = 0

    if request.method == 'POST':
        code = request.form.get('code')
        parser = yacc.yacc()

        try:
            parser.parse(code)
            if errores:
                result = "Código no aceptado."
            else:
                result = "Código aceptado."
                color = 1
        except Exception as e:
            errores.append(str(e))
            result = "Error al analizar el código."

        return render_template('index.html', code=code, errores=errores, color=color, resultado=result)
    return render_template('index.html', code=None)
