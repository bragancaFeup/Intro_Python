
"""
# Autor:  Bragança C.
# Data: 2019
# Objectivo: Numa lista de N valores determina:
# maximo, minimo, numero de maximos ede minimos e posiçoes.
# Variáveis:
N   #  Tamanho da lista
ValorActual #  Valor a ser analisado no momento
"""

N = int(input("Insira o tamanho da lista"))
ValorActual = int(input("Insira o primeiro valor da lista"))

Minimo = ValorActual
Maximo = ValorActual
NMaximos = 1
NMinimos = 1
PosMax=1
PosMin=1
K = 2
while  K <= N:
    ValorActual = int(input("Insira o próximo valor"))
    if ValorActual > Maximo:
        Maximo = ValorActual
        PosMax = K
        NMaximos = 1
    elif ValorActual == Maximo:
        NMaximos = NMaximos + 1

    if ValorActual < Minimo:
        Minimo = ValorActual
        PosMin = K
        NMinimos = 1
    elif ValorActual ==Minimo:
        NMinimos = NMinimos + 1

    K = K + 1

print(    "O valor máximo da lista foi {} ocorreu  {} vezes. Sendo que a primeira foi na {} posição.".format(Maximo, NMaximos ,PosMax))
print(    "O valor minimo da lista foi {} ocorreu  {} vezes. Sendo que a primeira foi na {} posição.".format(Minimo, NMinimos ,PosMin))

