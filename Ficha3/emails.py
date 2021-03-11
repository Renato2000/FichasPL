# Detação de endereços de email
import re

email = re.compile(r'(([a-zA-Z0-9_]+\.)*[a-zA-Z0-9_]+@([a-zA-Z0-9_]+\.)*[a-zA-Z0-9_]+)')

emails = []

n = int(input())

for i in range(n):
    linha = input()
    r = email.findall(linha) 
    if r:
        for(x,_,_) in r:
            emails.append(x)

emails.sort()
print(';'.join(emails))