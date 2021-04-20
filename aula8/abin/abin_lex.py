# abin_lex
# T = {num, '(', ')'}
# ABin -> '(' num ABin ABin ')'
#      | '(' ')'

import ply.lex as lex

tokens = ['num']
literals = ['(', ')'] # os literals não precisão de exp reg

t_num = r'[+\-]?\d+' # como não temos de fazer nada com ele, a exp reg chega

t_ignore = " \t\n"

def t_error(t):
    print("Carácter ilegal: ", t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()