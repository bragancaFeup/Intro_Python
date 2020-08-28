""""
Autor: Bragança / Brito, A. E. S. C.
Data: 2019
Exemplo do uso da função random

 Determinar a frequência de saída dos valores de 1 a 6
 em N lançamentos de um dado

"""
import random

N = int(input("Nº de lançamentos:"))

C = [0] * 7
K = 1

K = 1
while K <= N:
    J = int(6 * random.random()) + 1
    C[J] = C[J] + 1
    K = K + 1

for K in range(1, 6 + 1):
    print(K, "- ", 100 * C[K] / N, "%")
