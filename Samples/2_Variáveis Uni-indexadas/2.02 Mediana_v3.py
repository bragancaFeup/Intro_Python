""""
Autor: Bragança / Brito, A. E. S. C.
Data: 2019
Numa lista de N valores determinar a Mediana - N ímpar
ex:
Lista = [3, 4, 2, 6, 7]
N=5
Mediana = 4

"""


Lista = [3, 4, 2, 6, 7]
N=len(Lista)

Contador = 0
K=0
while K < N and Contador != int(N / 2):

    Contador = 0

    J = 0
    while J < N:

        if Lista[J] < Lista[K] :
            Contador = Contador + 1
        J = J + 1


    if Contador == int(N / 2) :
        Mediana = Lista[K]
    K = K + 1

print("Mediana = " , Mediana)

#
Lista.sort()
print("Medianaby Python= " , Lista[int(N/2)])