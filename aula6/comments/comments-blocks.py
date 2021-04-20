import ply.lex as lex
import sys

# Context Conditions
states = (
    ('comment', 'exclusive'),
    ('block', 'inclusive'),
)

# Tokens
tokens = ['CBEGIN', 'CEND', 'CONTENT', 'BBEGIN', 'BEND']

# Rules for initial state
def t_CBEGIN(t):
    r'/\*'
    t.lexer.push_state('comment')

def t_BBEGIN(t):
    r'\{'
    print('Entrei num bloco...')
    t.lexer.push_state('block')

def t_CONTENT(t): # esta regra tem de ficar em ultimo pq vai apanhar smp as outras
    r'.|\n'
    print(t.value,end="")

# Rules for comment state
def t_comment_CEND(t):
    r'\*/'
    t.lexer.pop_state()

def t_comment_CONTENT(t):
    r'.|\n'
    t.lexer.skip(1)

# Rules for block state
def t_block_BEND(t):
    r'\}'
    print('Sai dum bloco...')
    t.lexer.pop_state()

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