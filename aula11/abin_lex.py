import ply.lex as lex

tokens = ['NUM', 'AP', 'FP']

t_NUM = r'\d+'
t_AP = r'\('
t_FP = r'\)'

t_ignore = " \t\n"

def t_error(t):
    t.lexer.skip(1)
    return t


lexer = lex.lex()

'''
import sys
for linha in sys.stdin:
    lex.input(linha)
    for tok in lexer:
        print(tok) # Devolve o type, , a linha e a coluna
'''