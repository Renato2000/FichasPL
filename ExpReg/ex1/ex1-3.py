import re

f = open("file.txt", "r")

nome_EU = re.search(r'^EU=(.+)$', f)
nome_ELE = re.search(r'^ELE=(.+)$', f)

for linha in f:
    (new_text, n) = re.subn(r'(?i:ELE:)')
