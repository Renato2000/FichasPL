import re
import sys

def xml2html(texto):
    if res := re.search(r'encoding\s*=\s*(\"[^"]+\")', texto):
        print(f'<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Relatório</title>\n\t\t<meta charset={res.group(1)}/>\n\t</head>')

    elif (re.search(r'<relatorio>', texto)):
        print("\t<body>")

    elif (re.search(r'<\/relatorio>', texto)):
        print("\t</body>\n</html>")

    elif res := re.search(r'<titulo>((.|\n)*)<\/titulo>', texto):
        print("\t\t<h1>", res.group(1), "</h1>", sep='')

    elif res := re.search(r'<data>((.|\n)*)<\/data>', texto):
        print("\t\t<h2>", res.group(1), "</h2>", sep='')

    elif (re.search(r'<autores>', texto)):
        print("\t\t<h3>Autores</h3>\n\t\t<ul>")

    elif (re.search(r'<\/autores>', texto)):
        print("\t\t</ul>")

    elif (re.search(r'<autor>', texto)):
        print("\t\t\t<li>", end='', sep='')

    elif (re.search(r'<\/autor>', texto)):
        print("</li>")

    elif res := re.search(r'<nome>((.|\n)*)<\/nome>', texto):
        print(res.group(1), end='', sep='')

    elif res := re.search(r'<numero>((.|\n)*)<\/numero>', texto):
        print(" (", res.group(1), end=')', sep='')

    elif res := re.search(r'<email>((.|\n)*)<\/email>', texto):
        print(": ", res.group(1), end='', sep='')

    elif (re.search(r'<descricao>', texto)):
        print("\t\t<h3>Resumo</h3>")

    elif (re.search(r'<\/descricao>', texto)):
        pass

    else: # para as linhas de texto livre
        print("\t\t<p>", texto.lstrip().rstrip(), "</p>", sep='')


def formata(texto):
    resto = ""
    resultado = ""

    print(texto)

    resultado = re.search(r'^<[^>]+>[^<]*(<\/[^>]+>)?', texto, )
    resto = re.sub(r'^<[^>]+>[^<]*(<\/[^>]+>)?', texto, "", count=1)

    print(resultado)
    print(resto)

    return (resultado, resto)

#------------- Programa principal -------------
file = open("relatorio.xml", 'r')

resto = ""

for linha in file:
    (nova_lina, resto) = formata(linha + resto)
    xml2html(nova_lina)
