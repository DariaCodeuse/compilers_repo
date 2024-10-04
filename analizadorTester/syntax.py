import ply.yacc as yacc
from lex import tokens

# Definir la gramática
def p_declaracion_variable(p):
    '''declaracion : tipo lista_identificadores SEMICOLON
                   | tipo EQUALS lista_identificadores SEMICOLON'''
    print(f"Declaración de tipo '{p[1]}': {p[2]}")

def p_tipo(p):
    '''tipo : INT
             | FLOAT
             | CHAR
             | DOUBLE'''
    p[0] = p[1]

def p_lista_identificadores(p):
    '''lista_identificadores : IDENTIFIER
                              | lista_identificadores COMMA IDENTIFIER'''
    if len(p) == 2:
        p[0] = [p[1]]  # Solo un identificador
    else:
        p[0] = p[1] + [p[3]]  # Añadir identificador a la lista

# Otras reglas...

# Crear el parser
parser = yacc.yacc()

# Probar el parser
codigo = """
int a, b, c;
float = x, y;
"""

parser.parse(codigo)
