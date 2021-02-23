import re

inputFromUser = input(">> ")
while inputFromUser != "":
    y = re.search(r'^\([+-]?([1-8]\d(.\d+)?|90(.0+)?),\s[+-]?1?(80(.0+)?|[0-7]\d(.\d+)?)\)$', inputFromUser)
    if y:
        print("válido")
    else:
        print("inválido")
    inputFromUser = input(">> ")
