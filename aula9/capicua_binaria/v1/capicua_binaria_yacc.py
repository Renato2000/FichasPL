import ply.yacc as yacc

from capicua_binaria_lex import tokens

def p_Capicua_vazia(p):
    "Capicua : "
    p[0] = ""

def p_Capicua_zero(p):
    "Capicua : zero"
    p[0] = "0"

def p_Capicua_um(p):
    "Capicua : um"
    p[0] = "1"

def p_Capicua_zeros(p):
    "Capicua : zero Capicua zero"
    p[0] = "0" + p[2] + "0"

def p_Capicua_uns(p):
    "Capicua : um Capicua um"
    p[0] = "1" + p[2] + "1"


# Build the parser
parser = yacc.yacc()

# Read input and parse
import sys

for linha in sys.stdin:
    result = parser.parse(linha)
    print("Frase válida: ",result)
