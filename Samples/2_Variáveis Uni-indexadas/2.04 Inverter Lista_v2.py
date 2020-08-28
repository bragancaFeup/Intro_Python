""""
Autor: Bragança / Brito, A. E. S. C.
Data: 2019
# Objectivo: Dado um vector de dimensão N trocar
# os seus elementos por forma a que estes fiquem
# colocados na ordem inversa da inicial
# Variáveis:
#         Dim N As Integer # Numero de valores da lista
#         Dim Lista[100] As Single
#         Dim Temp As Single


"""

N = int(input("Por favor insira o número de elementos da lista"))

Lista=[None]*N
K = 0
while K < N:
    Lista[K] = int(input("Por favor insira o elemento seguinte da lista"))
    K = K + 1

K = 0
while K <= N / 2:
    Lista[K], Lista[N - K-1 ]= Lista[N - K-1 ],Lista[K]

    K = K + 1

print("Invertendo a ordem, a lista fica: ")

K = 0
while K < N:
    print(Lista[K])

    K = K + 1

