import re

musicas = {}

f = open('arqson.txt', 'r')

for linha in f:
    res = re.split(r'::',linha)
    if res:
        if res[1] in musicas:
            musicas[res[1]] += 1
        else:
            musicas[res[1]] = 1

for regiao in musicas:
    print("Regiao:", regiao, " Musicas:", musicas[regiao])
