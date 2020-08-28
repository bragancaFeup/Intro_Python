"""
# Autor:  Bragança
# Data: 2019
# Objectivo: Dados dois números determinar qual o maior
# Variáveis:
# Valor1, Valor2 Valores dados
# Maximo Valor máximo
"""
Valor1 = float(input("Primeiro valor: "))
Valor2 = float(input("Segundo valor: "))

if Valor1 > Valor2:
    Maximo = Valor1
else:
    Maximo = Valor2

print("Valor máximo = " + str(Maximo))
