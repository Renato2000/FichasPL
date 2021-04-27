import ply.yacc as yacc

from capicua_binaria2_lex import tokens

def p_Capicua_zeros(p):
    "Capicua : zero ContZ"
    p[0] = "0" + p[2]

def p_Capicua_uns(p):
    "Capicua : um ContU"
    p[0] = "1" + p[2]

def p_Capicua_vazio(p):
    "Capicua : "
    p[0] = ""

def p_ContZ_zero(p):
    "ContZ : Capicua zero"
    p[0] = p[1] + "0"

def p_ContZ_vazia(p):
    "ContZ : "
    p[0] = ""

def p_ContU_um(p):
    "ContU : Capicua um"
    p[0] = p[1] + "1"

def p_ContU_vazia(p):
    "ContU : "
    p[0] = ""

# Build the parser
parser = yacc.yacc()

# Read input and parse
import sys

for linha in sys.stdin:
    result = parser.parse(linha)
    print("Frase válida: ",result)
