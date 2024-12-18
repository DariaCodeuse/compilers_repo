
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DECIMAL DIVI MULTI NUMERO PABIERTO PCERRADO RESTA SUMAinicio : inicio SUMA medio\n              | inicio RESTA medio\n              | mediomedio : medio MULTI final\n              | medio DIVI final\n              | finalfinal : PABIERTO inicio PCERRADO\n              | NUMERO\n              | DECIMAL'
    
_lr_action_items = {'PABIERTO':([0,4,7,8,9,10,],[4,4,4,4,4,4,]),'NUMERO':([0,4,7,8,9,10,],[5,5,5,5,5,5,]),'DECIMAL':([0,4,7,8,9,10,],[6,6,6,6,6,6,]),'$end':([1,2,3,5,6,12,13,14,15,16,],[0,-3,-6,-8,-9,-1,-2,-4,-5,-7,]),'SUMA':([1,2,3,5,6,11,12,13,14,15,16,],[7,-3,-6,-8,-9,7,-1,-2,-4,-5,-7,]),'RESTA':([1,2,3,5,6,11,12,13,14,15,16,],[8,-3,-6,-8,-9,8,-1,-2,-4,-5,-7,]),'PCERRADO':([2,3,5,6,11,12,13,14,15,16,],[-3,-6,-8,-9,16,-1,-2,-4,-5,-7,]),'MULTI':([2,3,5,6,12,13,14,15,16,],[9,-6,-8,-9,9,9,-4,-5,-7,]),'DIVI':([2,3,5,6,12,13,14,15,16,],[10,-6,-8,-9,10,10,-4,-5,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,4,],[1,11,]),'medio':([0,4,7,8,],[2,2,12,13,]),'final':([0,4,7,8,9,10,],[3,3,3,3,14,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> inicio SUMA medio','inicio',3,'p_inicio','syntax.py',7),
  ('inicio -> inicio RESTA medio','inicio',3,'p_inicio','syntax.py',8),
  ('inicio -> medio','inicio',1,'p_inicio','syntax.py',9),
  ('medio -> medio MULTI final','medio',3,'p_medio','syntax.py',19),
  ('medio -> medio DIVI final','medio',3,'p_medio','syntax.py',20),
  ('medio -> final','medio',1,'p_medio','syntax.py',21),
  ('final -> PABIERTO inicio PCERRADO','final',3,'p_final','syntax.py',35),
  ('final -> NUMERO','final',1,'p_final','syntax.py',36),
  ('final -> DECIMAL','final',1,'p_final','syntax.py',37),
]
