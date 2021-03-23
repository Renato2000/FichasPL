import re

musicas = []

f = open('arqson.txt', 'r')

regiao = input("Regiao>> ")

for linha in f:
    res = re.split(r'::',linha)
    if res and res[1] == regiao:
        musicas.append(res[2])

print("Encontrei ", len(musicas), " que são: ", musicas)
