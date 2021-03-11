#Determinar se um determinado número de segurança social da India  é válido ou não.
#Na Índia, o número de segurança social atribuído a cada cidadão segue o
#seguinte formato:
#\begin{verbatim}
#    <char><char><char><char><char><digit><digit><digit><digit><char>
#\end{verbatim}
#Em que \texttt{<char>} corresponde a uma letra maiúscula e \texttt{<digit>} a um dígito.

import re

inp = input("Comece por indicar o numero de linhas e depois escreva os NSS: ")
n = int(inp)
for i in range(n):
   inp = input()
   pan = re.search(r'[A-Z]{5}[0-9]{4}[A-Z]', inp)
   if(pan):
      print("YES")
   else:
      print("NO")