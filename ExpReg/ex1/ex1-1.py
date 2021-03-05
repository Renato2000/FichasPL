import re

f = open("file.txt", "r")

for linha in f:
    (new_text, n) = re.subn(r'^(?i:ELE:)', "" , linha)
    if n == 0:
        new_text = re.sub(r'^(?i:EU:)', "", linha)
    print(new_text)
