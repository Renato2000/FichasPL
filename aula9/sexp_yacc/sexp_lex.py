# calc_lex

import ply.lex as lex

tokens = ['num', 'id', 'ADD', 'SUB', 'MUL', 'DIV', 'READ', 'PRINT', 'SET', 'DUMP']
literals = ['(', ')']

def t_ADD(t):
    r'add'
t_SUB = r'sub'
t_MUL = r'mul'
t_DIV = r'div'
t_READ = r'read'
t_PRINT = r'print'
t_SET = r'set'
t_DUMP = r'dump'
t_num = r'\d+'
t_id = r'[a-z]'

t_ignore = " \t\n"

def t_error(t):
    print("Carácter ilegal: ", t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()