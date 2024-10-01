import ply.yacc as yacc
from lex import tokens, lexer

errors = []

def p_for_statement(p):
  '''for_statement : FOR LPAREN initialization SEMICOLON condition SEMICOLON update RPAREN LBRACE body RBRACE '''
  if not errors:
        print("Estructura del bucle 'for' correcta")

def p_initialization(p):
  '''initialization : INT IDENTIFIER EQUALS NUMBER '''

def p_condition(p):
  '''condition : IDENTIFIER LESS_EQUAL NUMBER '''

def p_update(p):
  '''update : IDENTIFIER INCREMENT
            | INCREMENT IDENTIFIER '''

def p_body(p):
  '''body : SYSTEM DOT OUT DOT PRINTLN LPAREN STRING PLUS IDENTIFIER RPAREN SEMICOLON '''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc(debug=False)


def parser_for_statement(code):
    global errors
    errors = []
    lexer.lineno = 1
    result = parser.parse(code, lexer=lexer)
    return errors
