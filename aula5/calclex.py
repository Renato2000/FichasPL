# calclex.py
#   tokenizer para uma máquina de calcular
#
#       in: (3-1)*5+8/3
#       out: PA NUM SUB NUM PF MUL NUM ADD NUM DIV NUM -> atribuir nomes aos tokens
#----------------------------------------------------------------------------------

import ply.lex as lex
import sys

# Tocken declaration
tokens  = (
    'PA', 'PF',
    'ADD', 'SUB', # operadores aditivos
    'MUL', 'DIV', # opeadores multiplicativos
    'NUM'
)

# Token regex
t_PA = r'\('
t_PF = r'\)'
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'

# Token with some action code
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Tracking line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Characters to be ignored
t_ignore = " \t"

# Errors
def t_error(t):
    print(f"Caráter errado {t.value[0]}")
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex()

# reading input
for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        print(tok)