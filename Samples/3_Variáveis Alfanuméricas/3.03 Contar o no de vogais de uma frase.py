""""
Autor: Bragança / Brito, A. E. S. C.
Data: 2019

# Contar o no de vogais de uma frase

"""



Frase = input("Frase =")
NumCar = len(Frase)
caracteres = []
for I in range (NumCar):     #Coloca os caracteres da frase num vector
    caracteres.append(Frase[ I])

NumVogais = 0
for I in range (NumCar):
    letra = caracteres[I]
    if letra >= "a" and letra <= "z":   #Se for uma letra minúscula passa para maiúscula
        letra =letra.upper()
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U" : #Caso seja uma vogal actualiza o contador
        NumVogais = NumVogais + 1

print(f"No de vogais =  {NumVogais}")