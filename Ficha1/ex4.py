import re

inputFromUser = input(">> ")
while inputFromUser != "":
    y = re.search(r'\d{2}((-\d{2}){3}|:(\d{2}){3}|(...\d{2}){3})', inputFromUser)
    if y:
        print("válido")
    else:
        print("inválido")
    inputFromUser = input(">> ")
