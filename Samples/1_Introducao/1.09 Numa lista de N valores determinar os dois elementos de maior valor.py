"""


# Autor: Brito, A. E. S. C. / Bragança C.
# Data:2019
# Objectivo: Numa lista de N valores determinar os dois elementos de
#  maior valor.
# Assumir que estes valores são distintos

# Variáveis:
N           # Número de valores da lista
valor       # Valores da lista
K           # Índice do ciclo
Maximo1     # Maior valor da lista
Maximo2     # Segundo maior valor da lista
"""

N = int(input("Número de valores da lista: "))

# Lê os dois primeiros valores da lista e faz Maximo1 igual
# ao maior dos dois e Maximo2 igual ao menor dos dois valores

valor = int(input("Valor: "))
Maximo1 = valor

valor = int(input("Valor: "))

if valor > Maximo1:
    Maximo2 = Maximo1
    Maximo1 = valor
else:
    Maximo2 = valor


# Ciclo de leitura e determinação dos dois maiores valores
K = 3
while K <= N:
    valor = int(input("Valor: "))
    if  valor > Maximo1:
        # Se o valor lido é superior ao máximo dos anteriores
        Maximo2 = Maximo1
        Maximo1 = valor
    elif valor > Maximo2:
        # Se o valor lido é superior ao segundo maior valor
        # dos valores anteriores
        Maximo2 = valor
    K = K + 1


print("Maior valor = {}  2º. Maior valor = {}".format(Maximo1, Maximo2))