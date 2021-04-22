import sys
import ply.yacc as yacc

from lista_compras_lex import tokens

# Production rules
def p_Lista(p):
    "Lista : Seccoes"
    print("+--------------------------------------------+")
    print("\tValor total das compras:", p[1])
    print("+--------------------------------------------+")

def p_Seccoes_seccao(p):
    "Seccoes : Seccoes Seccao"
    p[0] = p[1] + p[2]

def p_Seccoes_empty(p):
    "Seccoes : "
    p[0] = 0

def p_Seccao(p):
    "Seccao : ID ':' Produtos"
    p[0] = p[3]
    if p[1] in p.parser.seccoes:
        print("[Aviso] Secções repetidas: " + p[1])
    else:
        p.parser.seccoes.add(p[1])

def p_Produtos_produto(p):
    "Produtos : Produto"
    p[0] =p[1]
    
def p_Produtos_produtos(p):
    "Produtos : Produtos Produto"
    p[0] =p[1] + p[2]
  
def p_Produto(p):
    "Produto : '-' INT SEP ID SEP FLOAT SEP INT ';'"
    p[0] = p[6] * p[8]
    info_produto = {
        'name' : p[4],
        'price' : p[6],
    }
    if p[2] in p.parser.produtos:
        if info_produto == p.parser.produtos[p[2]]:
            print("[Aviso] Múltiplas entradas do mesmo produto com o id:", p[2])
        else:
            print("[Erro] Produtos diferentes com o mesmo id:", p[2])
    else:
        p.parser.produtos[p[2]] = info_produto

def p_error(p):
    print('Syntax error!')

# Build the parser
parser = yacc.yacc()

# State
parser.seccoes = set()
parser.produtos = dict()

# Read input and parse
content = ""
for linha in sys.stdin:
    content += linha

parser.parse(content)
