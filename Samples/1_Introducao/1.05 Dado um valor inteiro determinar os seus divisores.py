"""
Autor: Bragança
        # Data: 2019
        # Objectivo: Dado um valor inteiro determinar os seus divisores.
        # Variáveis:
        Dim Valor As Integer # Valor dado
        Dim LimDiv As Integer # Valor máximo dos potenciais divisores do valor dado
        Dim Divisor As Integer # Potenciais divisores do valor dado
        Dim Quoc As Integer # Quociente inteiro de Valor/Divisor
        Dim Resto As Integer # Resto da divisão inteira de Valor/Divisor
"""

Valor = int(input("Valor: "))

LimDiv = int(Valor / 2)  # Nenhum valor superior à sua
# metade pode ser seu divisor
# excepto ele próprio
# Ciclo para obtenção dos potenciais divisores do valor dado
Divisor = 1
while Divisor <= LimDiv:
    Quoc = int(Valor / Divisor)
    Resto = Valor - Quoc * Divisor
    if Resto == 0:
        print("Divisores " + str(Divisor))  # É divisor do Valor dado

    Divisor = Divisor + 1

print("Divisores {0} ".format(Valor))  # Todo o número é divisor de si próprio
