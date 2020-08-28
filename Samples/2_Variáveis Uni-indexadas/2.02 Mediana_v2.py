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

for ValorK in Lista:
    Contador = 0

    for ValorJ in Lista:
        if ValorJ < ValorK:
            Contador = Contador + 1
    if Contador == int(N / 2):
        Mediana = ValorK

print("Mediana = " + str(Mediana))