import re

latlog = re.compile(r'^\([+-]?([1-8]?\d(.\d+)?|90(\.0+)?),\s[+-]?((([1-9]\d|1[0-7]\d)(\.\d+)?)|180(\.0+)?\)$)')
#latlog = re.compile(r'^\([+-]?([1-8]\d(.\d+)?|90(\.0+)?),\s[+-]?1?(80(.0+)?|[0-7]\d(.\d+)?)\)$')

inputFromUser = input(">> ")
while inputFromUser != "":
    res = latlog.search(inputFromUser)
    if res:
        print("válido")
    else:
        print("inválido")
    inputFromUser = input(">> ")
