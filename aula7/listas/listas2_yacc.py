# listas-yacc.py
#
# Listas heterogéneos: inteiros e alfanuméricos
#
# [78]
# [1, 2, 3]
# [a, barco]
# [121, asa, c45]
#
# T = {number, '[', ']', alfanum, ','}
# N = {Elementos}
# S = Lista
#
# p1: Lista -> '[' Elementos ']'
# p1.5: Lista -> '[' ']'   #não podemos especificar em Elementos, porque iríamos aceitar [,1]
# (p2: Elementos -> €)
# p2: Elementos -> Elemento
# (p3: Elementos -> Elemento ',' Elementos)    # esta gramatica é recursiva à diretia -> os parsers LALR (como o ply) preferem recursividade à esquerda
# p3: Elementos -> Elemento ',' Elementos
# p4, p5: Elemento -> alfanum | number
#

import ply.yacc as yacc
from listas_lex import tokens

def p_Lista(p):
    "Lista : PA Elementos PF"
    pass

def p_Lista_empty(p):
    "Lista : PA PF"
    pass

def p_Elementos(p):
    "Elementos : Elementos VIRG Elemento"
    p.parser.elems += 1

def p_Elementos_Elemento(p):
    "Elementos : Elemento"
    p.parser.elems = 1

def p_Elemento_number(p):
    "Elemento : number" # p[0] -> Elemento   p[1] -> number 
    p.parser.numbers.append(p[1]) # p tem associado um vetor com os elementos, e como queremos o number, vamos ao p[1]

def p_Elementos_alfanum(p):
    "Elementos : alfanum"
    p.parser.numbers.append(p[1])

def p_error(p):
    print("Erro sintático: ", p)
    parser.success = False

# Build the parser
parser = yacc.yacc()

# Read input and parse it by line
import sys

for linha in sys.stdin:
    parser.success = True
    parser.numbers = []
    parser.alfanum = []
    parser.elems = 0
    parser.parse(linha)

    if parser.success:
        print("Frase válida reconhecida: ", linha)
        print("Número de elementos: ", parser.elems)
        print("Números: ", parser.numbers)
        print("Alfanuméricos: ", parser.alfanum)
    else:
        print("Frase inválida. Corrija e tente de novo...")
