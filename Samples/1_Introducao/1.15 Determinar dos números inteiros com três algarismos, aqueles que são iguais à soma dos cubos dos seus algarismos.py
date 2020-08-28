"""
# Autor: Bragança
# Data: 2019
# Objectivo: Determinar dos números inteiros com três algarismos
#  aqueles que são iguais à soma dos cubos dos seus algarismos.
# Variáveis:
 NumInt  # Números inteiros de três algarismos
 AlgCen  # Algarismo das centenas
 AlgDez  # Algarismo das dezenas
 AlgUni  # Algarismo das unidades
 Aux  # Variável auxiliar
 SomCub  # Soma dos cubos

"""

# Ciclo para obtenção dos números inteiros de 3 algarismos
for NumInt in range(100, 999):

    Aux = int(NumInt / 10)
    AlgUni = NumInt - Aux * 10  # Algarismo das unidades
    AlgCen = int(Aux / 10)  # Algarismo das centenas
    AlgDez = Aux - AlgCen * 10  # Algarismo das dezenas
    SomCub = AlgCen ** 3 + AlgDez ** 3 + AlgUni ** 3

    if NumInt == SomCub:  # NumInt é igual à soma dos cubos dos seus algarismos
        print(NumInt, AlgCen, AlgDez, AlgUni, SomCub)
