import re

musicas = []

f = open('arqson.txt', 'r')

for linha in f:
    res = re.split(r'::',linha)
    if res and re.search(r'Jesus', res[2]):
        musicas.append(res[2])

print("Encontrei ", len(musicas), " que são: ", musicas)
