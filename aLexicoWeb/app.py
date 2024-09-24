import ply.yacc as yacc
from flask import Flask, render_template, request
import json

resultado_lexema = []
reservada = ['IF']

tokens = reservada + ('identificador', 'suma')

t_PARIZQ = r'\('
t_suma = r'\+'

def t_IF(t):
  r'if'
  return t

def t_FOR(t):
  r'for'
  return t

def t_error(t):
  global resultado_lexema
  estado = "Token no Válido"
  resultado_lexema.append(estado)

def prueba(data):
  global resultado_lexema
  analizador = lex.lex
  analizador.input(data)

analizador = lex.lex()

if __name__ == '__main__':
  while True:
    data =  input
