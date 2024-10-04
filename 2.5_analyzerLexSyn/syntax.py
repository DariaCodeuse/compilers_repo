import ply.yacc as yacc
from lex import tokens, lexer

errors = []
succes = []

def p_funcion(p):
    '''funcion : PROGRAMA IDENTIFICADOR LPAREN RPAREN LBRACE estructura RBRACE'''
    if not errors:
        print("Ningun error sintáctico!")

def p_estructura(p):
    'estructura : variables entrada operacion impresion salida'
    pass  # Aquí podrías agregar lógica para almacenar declaraciones

def p_variables(p):
    '''variables : INT IDENTIFICADOR COMA IDENTIFICADOR COMA IDENTIFICADOR SEMICOLON '''
    print("Variables correctamente declaradas ")

def p_entrada(p):
    '''entrada : lectura lectura'''

def p_lectura(p):
    '''lectura : READ IDENTIFICADOR SEMICOLON'''

def p_operacion(p):
    '''operacion : IDENTIFICADOR IGUAL IDENTIFICADOR ADICION IDENTIFICADOR SEMICOLON'''

def p_impresion(p):
    '''impresion : PRINT LPAREN CADENA RPAREN'''

def p_salida(p):
    '''salida : END SEMICOLON'''

def p_error(p):
    if p:
        errors.append(f"Error de sintaxis en el token '{p.value}', línea {p.lineno}")
    else:
        errors.append("Error de sintaxis al final del archivo")

# Build the parser
parser = yacc.yacc(debug=False)


def parser_for_statement(code):
    global errors
    errors.clear()  # Limpiar errores previos
    lexer.lineno = 1
    parser.parse(code, lexer=lexer)
    return errors
