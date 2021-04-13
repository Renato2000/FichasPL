# par_yacc.py
# Linguagem dos parentesis
# ()
# ((()))
# ()()(())
# ()((()))(((())))
#
# p1 : Par -> '(' Par ')' Par
# p2 : Par -> vazio
#
# Reconhecimento de: ()()(())
#   Par =p1=> '(' Par ')' Par
#       =p2=> '(' ')' Par
#       =p1=> '(' ')' '(' Par ')' Par
#       =p2=> '(' ')' '(' ')' Par
#       =p1=> '(' ')' '(' ')' '(' Par ')' Par 
#       =p1=> '(' ')' '(' ')' '(' '(' Par ')' Par ')' Par 
#       =p2=> '(' ')' '(' ')' '(' '(' ')' Par ')' Par 
#       =p2=> '(' ')' '(' ')' '(' '(' ')' ')' Par 
#       =p2=> '(' ')' '(' ')' '(' '(' ')' ')' 

import ply.yacc as yacc
from par_lex import tokens

def p_Par(p):
    "Par : PA Par PF Par"
    p.parser.pares += 1

def p_Par_empty(p):
    "Par : "

def p_error(p):
    print("Erro sintático: ", p)
    parser.success = False

# Build the parser
parser = yacc.yacc()

# Read input and parse it by line
import sys

for linha in sys.stdin:
    parser.success = True
    parser.pares = 0
    parser.parse(linha)

    if parser.success:
        print("Frase válida reconhecida: ", linha)
        print("Número de pares: ", parser.pares)
    else:
        print("Frase inválida. Corrija e tente de novo...")

