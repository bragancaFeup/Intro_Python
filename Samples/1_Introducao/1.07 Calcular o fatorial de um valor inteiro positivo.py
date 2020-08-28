"""
# Autor: Bragança
# Data: 2019
# Objectivo: Calcular o fatorial de um valor inteiro positivo.
# Variáveis:
    N           # Valor dado
    NFactorial  # Factorial do valor dado
"""

N = int(input("Valor: "))

NFactorial = 1

# Ciclo de cálculo de N factorial
while N != 0:
    NFactorial = NFactorial * N
    N = N - 1


print("Factorial ={} ".format(NFactorial))