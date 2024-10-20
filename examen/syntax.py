import ply.yacc as yacc
from lex import tokens, lexer

# Listas para almacenar errores, variables leídas, etc.
errors = []
check = []
check2 = []

# Producciones del analizador sintáctico para el código C#
def p_program(p):
    '''program : USING SYSTEM SEMICOLON NAMESPACE HELLOWORLD LBRACE class_definition RBRACE'''
    # Esta producción representa la estructura principal de un programa C#:
    # using System; namespace HelloWorld { ... }
    pass

def p_class_definition(p):
    '''class_definition : CLASS HELLO LBRACE method_definition RBRACE'''
    # Producción para la definición de una clase, como class Hello { ... }
    pass

def p_method_definition(p):
    '''method_definition : STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET ARGS RPAREN LBRACE statement_list RBRACE'''
    # Producción para la definición de un método, como Main(string[] args) { ... }
    pass

def p_statement_list(p):
    '''statement_list : statement statement_list
                      | statement'''
    # Lista de declaraciones dentro del método Main
    pass

def p_statement(p):
    '''statement : print_statement
                 | COMENTARIO
                 | empty'''
    # Declaraciones dentro del método: impresión, comentario o vacío.
    pass

def p_print_statement(p):
    '''print_statement : SYSTEM PUNTO CONSOLE PUNTO WRITELINE LPAREN CADENA RPAREN SEMICOLON'''
    # Producción para la impresión: System.Console.WriteLine("Hello World!");
    pass

# Producción vacía para manejar estructuras opcionales
def p_empty(p):
    '''empty : '''
    pass

# Manejo de errores
def p_error(p):
    if p:
        errors.append(f"Error de sintaxis en el token '{p.value}', línea {p.lineno}")
    else:
        errors.append("Error de sintaxis al final del archivo")

# Construir el parser
parser = yacc.yacc()

# Función para ejecutar el parser
def parser_for_statement(code):
    global errors
    errors.clear()  # Limpiar errores previos
    lexer.lineno = 1
    parser.parse(code, lexer=lexer)
    return errors
