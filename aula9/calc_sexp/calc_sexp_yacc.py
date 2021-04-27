# calc_yacc

import ply.yacc as yacc
from calc_sexp_lex import tokens

# Production rules
def p_Comando_ler(p):
    "Comando : '?' id"
    print("(read ", p[2], ")")

def p_Comando_escrever(p):
    "Comando : '!' Exp"
    print("(print ", p[2], ")")

def p_Comando_atrib(p):
    "Comando : id '=' Exp"
    print("(set ", p[1], " ", p[3], ")")

def p_Comando_despejar(p):
    "Comando : '!' '!'"
    print("(dump)")

def p_Exp_add(p):
    "Exp : Exp '+' Termo"
    p[0] = "(add " + p[1] + " " + p[3] + ")"

def p_Exp_sub(p):
    "Exp : Exp '-' Termo"
    p[0] = "(sub " + p[1] + " " + p[3] + ")"

def p_Exp_termo(p):
    "Exp : Termo"
    p[0] = p[1]

def p_Termo_mul(p):
    "Termo : Termo '*' Fator"
    p[0] = "(mul " + p[1], " " + p[3] + ")"

def p_Termo_div(p):
    "Termo : Termo '/' Fator"
    if(p[3] != '0'):
        p[0] = "(div " + p[1] + " " + p[3] + ")"
    else: 
        print("Erro: divisão por 0. A continuar com o dividendo: ", p[1])
        p[0] = p[1]

def p_Termo_fator(p):
    "Termo : Fator"
    p[0] = p[1]

def p_Fator_group(p):
    "Fator : '(' Exp ')'"
    p[0] = p[2]

def p_Fator_num(p):
    "Fator : num"
    p[0] = p[1]

def p_Fator_id(p):
    "Fator : id"
    p[0] = p[1]

def p_error(p):
    print("Syntax error in input: ", p)

# Build the parser
parser = yacc.yacc()

# Read input and parse it by line
import sys

for linha in sys.stdin:
    result = parser.parse(linha)
