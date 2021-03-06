import ply.lex as lex
import sys

# Context Conditions
states = (
    ('comment', 'exclusive'),
)

# Tokens
tokens = ['CBEGIN', 'CEND', 'CONTENT']

# Rules for initial state
def t_CBEGIN(t):
    r'/\*'
    t.lexer.begin('comment')

def t_CONTENT(t): # esta regra tem de ficar em ultimo pq vai apanhar smp as outras
    r'.|\n'
    print(t.value,end="")

# Rules for comment state
def t_comment_CEND(t):
    r'\*/'
    t.lexer.begin('INITIAL')

def t_comment_CONTENT(t):
    r'.|\n'
    t.lexer.skip(1)

# Rules for all
def t_ANY_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# reading input
for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        pass