import ply.yacc as yacc
from lex import tokens, lexer

errors = []
succes = []
check = []
check2 = []

def p_funcion(p):
    '''funcion : PROGRAMA IDENTIFICADOR LPAREN RPAREN LBRACE estructura RBRACE'''

def p_estructura(p):
    'estructura : variables entrada operacion impresion salida'
    # Aquí podrías agregar lógica para almacenar declaraciones
    pass

def p_variables(p):
    '''variables : INT VARIABLE COMA VARIABLE COMA VARIABLE SEMICOLON '''
    for i in p[2], p[4], p[6]:
        check.append(i)

def p_entrada(p):
    '''entrada : lectura lectura'''

def p_lectura(p):
    '''lectura : READ VARIABLE SEMICOLON'''
    if p[2] not in check:
        errors.append(f"Variable '{p[2]}' no declarada antes")
    else:
        check2.append(p[2])

def p_operacion(p):
    '''operacion : VARIABLE IGUAL VARIABLE ADICION VARIABLE SEMICOLON'''
    if p[1] not in check:
        errors.append(f"Variable '{p[1 ]}' no declarada antes")
    
    if p[3] not in check:
        errors.append(f"Variable '{p[3]}' no declarada antes")
    elif p[3] not in check2:
        errors.append(f"Variable '{p[3]}' no leída antes")

    if p[5] not in check:
        errors.append(f"Variable '{p[5]}' no declarada antes")
    elif p[5] not in check2:
        errors.append(f"Variable '{p[5]}' no leída antes")

def p_impresion(p):
    '''impresion : PRINT LPAREN COMILLA CADENA CADENA CADENA COMILLA RPAREN'''

def p_salida(p):
    '''salida : END SEMICOLON'''

def p_error(p):
    if p:
        if p.type == "CADENA":
            pass 
        else:
            errors.append(f"Error de sintaxis en el token '{p.value}', línea {p.lineno}")
    else:
        errors.append("Error de sintaxis al final del archivo")

# Build the parser
parser = yacc.yacc()

def parser_for_statement(code):
    global errors
    errors.clear()  # Limpiar errores previos
    lexer.lineno = 1
    parser.parse(code, lexer=lexer)
    return errors
