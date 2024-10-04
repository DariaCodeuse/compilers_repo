
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADICION CADENA COMA END IDENTIFICADOR IGUAL INT LBRACE LPAREN PRINT PROGRAMA RBRACE READ RPAREN SEMICOLON SUMA VARIABLEfuncion : PROGRAMA IDENTIFICADOR LPAREN RPAREN LBRACE estructura RBRACEestructura : variables entrada operacion impresion salidavariables : INT IDENTIFICADOR COMA IDENTIFICADOR COMA IDENTIFICADOR SEMICOLON entrada : lectura lecturalectura : READ IDENTIFICADOR SEMICOLONoperacion : IDENTIFICADOR IGUAL IDENTIFICADOR ADICION IDENTIFICADOR SEMICOLONimpresion : PRINT LPAREN CADENA RPARENsalida : END SEMICOLON'
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,10,],[0,-1,]),'IDENTIFICADOR':([2,9,11,13,17,19,22,23,29,32,],[3,14,16,18,-4,24,28,-5,33,35,]),'LPAREN':([3,21,],[4,27,]),'RPAREN':([4,31,],[5,34,]),'LBRACE':([5,],[6,]),'INT':([6,],[9,]),'RBRACE':([7,25,30,],[10,-2,-8,]),'READ':([8,12,23,36,],[13,13,-5,-3,]),'COMA':([14,24,],[19,29,]),'PRINT':([15,37,],[21,-6,]),'IGUAL':([16,],[22,]),'SEMICOLON':([18,26,33,35,],[23,30,36,37,]),'END':([20,34,],[26,-7,]),'CADENA':([27,],[31,]),'ADICION':([28,],[32,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'funcion':([0,],[1,]),'estructura':([6,],[7,]),'variables':([6,],[8,]),'entrada':([8,],[11,]),'lectura':([8,12,],[12,17,]),'operacion':([11,],[15,]),'impresion':([15,],[20,]),'salida':([20,],[25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> funcion","S'",1,None,None,None),
  ('funcion -> PROGRAMA IDENTIFICADOR LPAREN RPAREN LBRACE estructura RBRACE','funcion',7,'p_funcion','syntax.py',8),
  ('estructura -> variables entrada operacion impresion salida','estructura',5,'p_estructura','syntax.py',13),
  ('variables -> INT IDENTIFICADOR COMA IDENTIFICADOR COMA IDENTIFICADOR SEMICOLON','variables',7,'p_variables','syntax.py',17),
  ('entrada -> lectura lectura','entrada',2,'p_entrada','syntax.py',21),
  ('lectura -> READ IDENTIFICADOR SEMICOLON','lectura',3,'p_lectura','syntax.py',24),
  ('operacion -> IDENTIFICADOR IGUAL IDENTIFICADOR ADICION IDENTIFICADOR SEMICOLON','operacion',6,'p_operacion','syntax.py',27),
  ('impresion -> PRINT LPAREN CADENA RPAREN','impresion',4,'p_impresion','syntax.py',30),
  ('salida -> END SEMICOLON','salida',2,'p_salida','syntax.py',33),
]
