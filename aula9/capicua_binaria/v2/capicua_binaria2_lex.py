# Capicua
# 
#  T = {0, 1}
# Capicua -> '0' ContZ
#          | '1' ContU
#          | vazio
# ContZ -> vazio
#        | Capicua '0'
# ContZ -> vazio
#        | Capicua '1'

import ply.lex as lex

tokens = ['zero', 'um']

t_zero = r'0'
t_um = r'1'

t_ignore = " \t\n"

def t_error(t):
    print("Caráter ilegal: ", t.value[0])
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex()