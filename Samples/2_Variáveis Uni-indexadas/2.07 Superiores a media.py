""""
Autor: Bragança / Brito, A. E. S. C.
Data: 2019

# Imprime os valores de uma lista que são superiores à média aritmética da lista

"""


N = int(input("Nº de valores"))

A=[None]*N
Soma = 0
I = 0
while I < N:
    A[I] = int(input("A[" + str(I) + "]="))
    Soma = Soma + A[I]
    I = I + 1

Media = Soma / N

I = 0
while I < N:
    if A[I] > Media:        # Se o valor é superior à média
        print("A[" , I , "]=" , A[I])
    I = I + 1
