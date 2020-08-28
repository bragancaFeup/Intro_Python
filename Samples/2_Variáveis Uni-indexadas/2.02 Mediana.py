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
N = len(Lista)

for K in range(0, N):
    Contador = 0


    for J in range(0, N):
        if Lista[J] < Lista[K]:
            Contador = Contador + 1
    if Contador == int(N / 2):
        Mediana = Lista[K]

print("Mediana = " + str(Mediana))