# calc_lex

import ply.lex as lex

tokens = ['num', 'id']
literals = ['(', ')', '+', '-', '*', '/', '?', '!', '=']

t_num = r'\d+'
t_id = r'[a-z]'

t_ignore = " \t\n"

def t_error(t):
    print("Carácter ilegal: ", t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()