import re

musicas = []

f = open('arqson.txt', 'r')

for linha in f:
    res = re.split(r'::',linha)
    if res and re.search(r'.mp3$', res[len(res)-3]):
        musicas.append(res[2])

print("Encontrei ", len(musicas), " que são: ", musicas)
