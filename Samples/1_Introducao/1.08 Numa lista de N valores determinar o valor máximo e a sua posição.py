"""


# Autor: Brito, A. E. S. C. / Bragança
# Data: 2019
# Objectivo: Numa lista de N valores determinar o valor máximo
# e a sua posição
# Variáveis:
    N       # Número de valores da lista
    Valor       # Valores da lista
    K           # Índice do ciclo
    Maximo      # Valor máximo
    PosMaximo   # Posição na lista do valor máximo
"""

N = int(input("Número de valores da lista: "))

Valor = int(input("Valor: "))  # Lê o primeiro valor da lista

# Considera o valor máximo igual ao primeiro valor da lista
Maximo = Valor
PosMaximo = 1

# Ciclo de leitura e determinação do valor máximo
K = 2
while K <= N:
    Valor = int(input("Valor: "))
    if Valor > Maximo:
        # Se o valor lido é superior ao máximo dos anteriores
        # actualiza o valor máximo e respectiva posição
        Maximo = Valor
        PosMaximo = K
    K = K + 1

print("Valor máximo = {} Posição = {}".format(Maximo, PosMaximo))
