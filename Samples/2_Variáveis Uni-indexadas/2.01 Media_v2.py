""""
Autor: Bragança / Brito, A. E. S. C.
Data: 2019
E Objectivo: Dada uma lista de N valores calcular a sua média aritmética.

    # Variáveis:
   # Soma As Single #Soma dos valores da lista
   # Media As Single #Média aritmética dos valores da lista

"""
N = int(input("Nº de valores da lista"))
Lista=[0]*N
K=0
while K < N:
    Lista[K] = int(input("Lista(" + str(K) + ")"))
    K = K + 1

Soma = 0    #Inicializa a variável Soma
#Ciclo de leitura e soma dos valores da lista
K = 0
while K < N:
    Soma = Soma + Lista[K]
    K = K + 1


Media = Soma / N #Calcula a média aritmética
print("Média aritmética = " + str(Media))
print (Lista)

