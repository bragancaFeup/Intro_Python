""""
Autor: Bragança / Brito, A. E. S. C.
Data: 2019

# Dado um conjunto de N números detetar quantos são diferentes entre si.
"""


N = int(input(" INSIRA O Nº DE VALORES :"))
Lista=[None]*N
K = 0
while K < N:
    Lista[K] = int(input("INTRODUZA OS VALORES:" + str(K) + "="))
    K = K + 1

NumDeDiferentes = 0
K = 0
while K < N:

    ContadorTemp = 0
    J = 0
    while J <= K:

        if Lista[J] == Lista[K]:
            ContadorTemp = ContadorTemp + 1

        J = J + 1

    if ContadorTemp == 1:
        NumDeDiferentes = NumDeDiferentes + 1

    K = K + 1

print("Nº DE VALORES DIFERENTES:" , NumDeDiferentes)
