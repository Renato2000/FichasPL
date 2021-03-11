# Deteção de tags HTML

''' 
Exemplo de input:
2
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.qt.com/lexamples.cfm">More Link Examples...</a></div>

Resultado:
a;div;p
'''

import re

tag = re.compile(r'<([a-z]+)\s*')

tags = []

n = int(input())

for i in range(n):
    linha = input()
    r = tag.findall(linha) 
    if r:
        for x in r:
            tags.append(x)

tags.sort()

tags = list( dict.fromkeys(tags) )

print(';'.join(tags))
