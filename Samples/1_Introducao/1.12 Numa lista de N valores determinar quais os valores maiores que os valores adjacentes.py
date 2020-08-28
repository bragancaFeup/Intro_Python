"""


# Título: Valores maiores que os adjacentes de uma lista de valores
# Autor: Brito, A. E. S. C.
# Data: 920102
# Objectivo: Numa lista de N valores determinar
#  quais os valores maiores que os valores adjacentes.
# Variáveis:
N       # Número de valores da lista
Valor   # Valores da lista
K       # Índice de ciclo

ValAnt  # Valor da lista anterior a Valor
ValSeg  # Valor da lista sequinte a Valor
# 
"""

N = int(input("Número de valores: "))

while N < 3:
    N = int(input("Número de valores: (N>2) "))


# Leitura dos dois primeiros valores da lista
ValAnt = float(input("Valor: "))
Valor = float(input("Valor: "))

if ValAnt > Valor:      # Se o primeiro valor é maior que o segundo
    MsgBox("O primeiro valor ({}) é maior que o segundo [{]} ".format( ValAnt,Valor))

# Ciclo de leitura e determinação dos valores maiores que os adjacentes
K = 3
while K <= N:
    ValSeg = float(input("Valor: "))
    if Valor > ValAnt and Valor > ValSeg:   # Se o valor é maior que os adjacentes
      print  ("Valor {} é maior que os adjacentes ({} e {}) ".format(Valor,ValAnt,ValSeg))
    ValAnt = Valor # O valor central passa a ser o anterior
    Valor = ValSeg # O valor seguinte passa a ser o central
    K = K + 1


if Valor > ValAnt:  # Se o último valor é maior que o penúltimo
    print("Valor {} é maior que os adjacentes ({} e {}) ".format(Valor, ValAnt, ValSeg))

