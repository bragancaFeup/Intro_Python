"""
#Autor:  Bragança
#Data: 2019
#Contar o nº de espaços de uma frase
 Frase      #Frase dada
 NumCar     #Nº de caracteres da frase
 Caracter   #Caracteres da frase
 i As       #var. auxiliar
 ContEsp    #Contador de espaços
"""


Frase = input("Frase")

#opção 1
NumCar = len((Frase))
ContEsp = 0
i=1

while i <= NumCar:   #Para cada caracter da frase
    Caracter = Frase[i-1]

    if Caracter == " ":  #Caso seja um espaço
        ContEsp = ContEsp + 1
    i=i+1
print("Nº de espaços = {}".format( ContEsp))

#opção 2

ContEsp=0
for Caracter in Frase:
    if Caracter == " ":  # Caso seja um espaço
        ContEsp = ContEsp + 1
    i = i + 1
print("Nº de espaços = {}".format(ContEsp))

