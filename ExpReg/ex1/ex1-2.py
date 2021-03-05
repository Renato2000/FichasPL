import re

f = open("file.txt", "r")

for linha in f:
    (new_text, n) = re.subn(r'^(?i:ELE:)', "Entrevistado", linha)
    if n == 0:
        new_text = re.sub(r'^(?i:EU:)', "Entrevistador", linha)
    print(new_text)
