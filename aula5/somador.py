# Somador on/off
#   -> semáforo está on de inicio
#   -> lê do input
#   -> reagir a estimulos:
#       r'[oO][nN]' -> ligar o semaforo
#       r'(o|O)(n|N)'
#       r'[oO][fF]{2}' -> desligar o semaforo
#       r'(o|O)(f|F)(f|F)'
#       r'=' -> escrever o valor acomulado
#       r'\d+' -> acrescentar o valor lido acomulado
#       qq outra coisa -> descartar

import sys
import re

# My state
soma = 0
semaforo = True

# Reading input
for linha in sys.stdin:
    if res := re.findall(r'([oO][nN])|([oO][fF]{2})|(=)|(\d+)', linha):
        for (on, off, pr, num) in res:
            if on:
                semaforo = True
            elif off:
                semaforo = False
            elif pr:
                print("O valor acumulado é ", soma)
            elif num:
                if semaforo:
                    soma = soma + int(num)
    else:
        pass
