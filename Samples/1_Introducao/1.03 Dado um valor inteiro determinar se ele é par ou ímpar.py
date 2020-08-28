"""
# Autor: Brito, A. E. S. C. / Bragança
# Data: 920102
# Objectivo: Dado um valor inteiro determinar se ele é par ou ímpar.
# Variáveis:
#  N   Número dado
#  Quoc   Quociente da divisão inteira de N por 2
#  Resto   Resto da divisão inteira de N por 2
"""


N = int(input("Valor: "))
Quoc = int(N / 2)
Resto = N - Quoc * 2

if Resto == 0:
    print("O Valor dado é par")
else:
    print("O Valor dado é ímpar")
