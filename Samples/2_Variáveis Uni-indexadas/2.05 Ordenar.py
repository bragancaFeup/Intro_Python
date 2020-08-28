""""
Autor: Bragança / Brito, A. E. S. C.
Data: 2019
# Objectivo: Dado um vetor de dimensão N ordenar os seus elementos por ordem crescente

"""

N = int(input("Por favor insira N"))


Lista=[None]*N
K = 0

while K < N :        # Ciclo que armazena a lista inserida
    Lista[K] = int(input("Por favor insira o próximo valor da lista"))
    K = K + 1

I = 0
while I < N -1 :  # Ciclo que vai percorrer todos os elementos da lista
    K = I + 1
    while K < N:
        if Lista[I] > Lista[K]:
            Temp = Lista[I]
            Lista[I] = Lista[K]
            Lista[K] = Temp
        K = K + 1
    I = I + 1

print("O vector ordenado fica: ")
K = 0
while K < N:
    print(Lista[K])
    K = K + 1

