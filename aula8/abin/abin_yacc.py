# abin_yacc
# ()
# ( 15 () ()))
# (30 (7 () ()) (43 (35 () ()) () ))
#
# Terminais = {simbolos, palavras reservadas (tem mais do que um caracter), terminais variáveis (à partida não sabemos quais são -> é o utilizador a introduzir)}
#
# p1 : Elemento -> Num
# p2 : No -> Elemento No No
#
# {
#   "root": num;
#   "left": null;
#   "right": null;
# }
#
# TO-DO: respeitar a identação

import ply.yacc as yacc
from abin_lex import tokens

# Production rules
def p_ABin(p):
    "ABin : '(' num ABin ABin ')'"
    p[0] = "{\n\t\"root\": " + p[2] + ",\n\t\"left:\" " + p[3] + ",\n\t\"right:\" " + p[4] + "\n}"

def p_ABin_empty(p):
    "ABin : '(' ')'"
    p[0] = "null"

def p_error(p):
    print("Syntax error in input: ", p)

# Build the parser
parser = yacc.yacc()

# Read input and parse it by line
import sys

for linha in sys.stdin:
    result = parser.parse(linha)
    print(result)
