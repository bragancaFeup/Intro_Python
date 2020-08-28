""""
Autor: Bragança / Brito, A. E. S. C.
Data: 2019

# Inverter os caracteres de uma frase

"""

Frase = input("Frase")

NumCar = len(Frase)
NovaFrase = ""

# for I in range(NumCar):
#     NovaFrase = NovaFrase + Frase[-I-1]

# ou

# for I in range(NumCar):
#     NovaFrase =  Frase[I] + NovaFrase

# ou

for I in range(NumCar-1,-1,-1):
    NovaFrase =  NovaFrase +Frase[I]


print("Frase invertida = " + NovaFrase)