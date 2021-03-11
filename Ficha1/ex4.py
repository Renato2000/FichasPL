import re

matricula = re.compile(r'(\d{2}((\.\.\.|-|:)\d{2}){3})')

matriculas = []

linha = input(">> ")

while(linha):
    res = matricula.findall(linha)
    if res:
        for (m,_,_) in res:
            matriculas.append(m)
            #print(m)

    print("Encontrei ", len(matriculas), " que são: ", matriculas)
    matriculas = []

    linha = input(">> ")
