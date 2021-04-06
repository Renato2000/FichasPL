import ply.lex as lex # Manual do Lex: dabeaz.com/ply/ply.html
import sys

# Tocken declaration
tokens  = (
    'ON', 'OFF',
    'PRINT', 'NUM'
)

# Token with some action code
def t_NUM(t):
    r'\d+'
    if t.lexer.semaforo:
        t.lexer.soma = t.lexer.soma + int(t.value)

def t_ON(t):
    r'[oO][nN]'
    t.lexer.semaforo = True

def t_OFF(t):
    r'[oO][fF]{2}'
    t.lexer.semaforo = False

def t_PRINT(t):
    r'='
    print("O valor acumulado é ", t.lexer.soma)

# Tracking line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Characters to be ignored
t_ignore = " \t"

# Errors
def t_error(t):
    #print(f"Caráter errado {t.value[0]}")
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex()

# My state
lexer.soma = 0
lexer.semaforo = True

# reading input
for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer: # equivalente a tok = lexer.token()
        print(tok)
