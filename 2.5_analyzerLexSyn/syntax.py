import ply.yacc as yacc
from lex import tokens, lexer

errors = []





# Build the parser
parser = yacc.yacc(debug=False)


def parser_for_statement(code):
    global errors
    errors.clear()  # Limpiar errores previos
    lexer.lineno = 1
    parser.parse(code, lexer=lexer)
    return errors
