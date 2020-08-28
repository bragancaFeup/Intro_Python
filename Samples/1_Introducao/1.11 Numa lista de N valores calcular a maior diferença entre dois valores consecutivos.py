"""
 Autor: Brito, A. E. S. C. / Bragança C.

# Data: 920102
# Objectivo: Numa lista de N valores calcular a maior diferença
#  entre dois valores consecutivos.

# Variáveis:

N   # Número de valores da lista
Valor   # Valores da lista
K   # Índice de ciclo
ValAnt  # Valor da lista anterior a Valor
Dif     # Diferença entre valores consecutivos
MaxDif  # Diferença máxima entre valores consecutivos
"""

N = int(input("Número de valores da lista: "))

ValAnt = float(input("primeiro valor da lista"))  # Leitura do primeiro valor da lista
MaxDif = 0  # Inicialização da diferença máxima

# Ciclo de leitura e determinação da diferença máxima

k = 2
while k <= N:
    Valor = float(input("Valor: "))
    Dif = abs(Valor - ValAnt)
    if Dif > MaxDif:  # Se a diferença é maior que a diferença máxima
        MaxDif = Dif
    ValAnt = Valor
    k = k + 1

print("Diferença máxima = {}".format(MaxDif))
