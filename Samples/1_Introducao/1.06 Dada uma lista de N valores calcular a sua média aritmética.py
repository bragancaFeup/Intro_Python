"""
# Autor: Brito, A. E. S. C. / Bragança,C.
        # Data: 2019
        # Objectivo: Dada uma lista de N valores calcular a sua média aritmética.

        # Variáveis:
         N          # Número de valores da lista
         Valor      # Valores da lista
         k          # Índice do ciclo
         Soma       # Soma dos valores da lista
         Media      # Média aritmética dos valores da lista
"""

N = int(input("Número de valores da lista: "))
Soma = 0  # Inicializa a variável Soma

# Ciclo de leitura e soma dos valores da lista
k = 1
while k <= N:
    Valor = float(input("Valor: "))
    Soma = Soma + Valor
    k = k + 1

Media = Soma / N  # Calcula a média aritmética

print("Média aritmética = {} ".format(Media))
