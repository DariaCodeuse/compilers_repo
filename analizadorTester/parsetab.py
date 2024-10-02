
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DOT EQUALS FOR IDENTIFIER INCREMENT INT LBRACE LESS_EQUAL LPAREN NUMBER OUT PLUS PRINTLN RBRACE RPAREN SEMICOLON STRING SYSTEMfor_statement : FOR LPAREN initialization SEMICOLON condition SEMICOLON update RPAREN LBRACE body RBRACE initialization : INT IDENTIFIER EQUALS NUMBER condition : IDENTIFIER LESS_EQUAL NUMBER update : IDENTIFIER INCREMENT\n            | INCREMENT IDENTIFIER body : SYSTEM DOT OUT DOT PRINTLN LPAREN STRING PLUS IDENTIFIER RPAREN SEMICOLON '
    
_lr_action_items = {'FOR':([0,],[2,]),'$end':([1,24,],[0,-1,]),'LPAREN':([2,28,],[3,29,]),'INT':([3,],[5,]),'SEMICOLON':([4,8,13,17,33,],[6,11,-2,-3,34,]),'IDENTIFIER':([5,6,11,16,31,],[7,9,15,20,32,]),'EQUALS':([7,],[10,]),'LESS_EQUAL':([9,],[12,]),'NUMBER':([10,12,],[13,17,]),'INCREMENT':([11,15,],[16,19,]),'RPAREN':([14,19,20,32,],[18,-4,-5,33,]),'LBRACE':([18,],[21,]),'SYSTEM':([21,],[23,]),'RBRACE':([22,34,],[24,-6,]),'DOT':([23,26,],[25,27,]),'OUT':([25,],[26,]),'PRINTLN':([27,],[28,]),'STRING':([29,],[30,]),'PLUS':([30,],[31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'for_statement':([0,],[1,]),'initialization':([3,],[4,]),'condition':([6,],[8,]),'update':([11,],[14,]),'body':([21,],[22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> for_statement","S'",1,None,None,None),
  ('for_statement -> FOR LPAREN initialization SEMICOLON condition SEMICOLON update RPAREN LBRACE body RBRACE','for_statement',11,'p_for_statement','syntax.py',7),
  ('initialization -> INT IDENTIFIER EQUALS NUMBER','initialization',4,'p_initialization','syntax.py',12),
  ('condition -> IDENTIFIER LESS_EQUAL NUMBER','condition',3,'p_condition','syntax.py',15),
  ('update -> IDENTIFIER INCREMENT','update',2,'p_update','syntax.py',18),
  ('update -> INCREMENT IDENTIFIER','update',2,'p_update','syntax.py',19),
  ('body -> SYSTEM DOT OUT DOT PRINTLN LPAREN STRING PLUS IDENTIFIER RPAREN SEMICOLON','body',11,'p_body','syntax.py',22),
]
