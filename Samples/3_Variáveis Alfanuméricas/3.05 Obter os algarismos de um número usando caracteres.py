""""
Autor: Bragança / Brito, A. E. S. C.
Data: 2019

Obter os algarismos de um número usando caracteres

"""


valorInteiro = int(input("valor ="))


valorString = str(valorInteiro)

for L in valorString:
    print(L)

# ou

for k in range(len(valorString)):
    print(valorString[k])

# ou

numeros=[]

for k in range(len(valorString)):
    numeros.append(valorString[k])

print(numeros)
