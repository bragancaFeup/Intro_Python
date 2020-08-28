
"""
# Autor: Bragança
# Data: 2009

gerar um número aleatório entre 1 e N (N dado) evitando, no
entanto, em chamadas consecutivas a obtenção de um mesmo número.

Dim Intervalo As Integer #  intervalo dos valores
Dim NumeroResultados As Integer
Dim NumeroAleatorio As Integer #  número aleatório
Dim Resultado As String
Dim Anterior As Integer
Dim I As Integer

"""
import random

Intervalo = int(input("Limite superior do intervalo"))
NumeroResultados = int(input("Numero de resultados"))

NumeroAleatorio = int(random.random() * Intervalo)
Anterior = NumeroAleatorio
Resultado = str( NumeroAleatorio)

I = 1
while I < NumeroResultados:
    NumeroAleatorio = int(random.random() * Intervalo)
    if NumeroAleatorio != Anterior :
        Resultado = Resultado + " , " + str(NumeroAleatorio)
    I = I + 1
    Anterior = NumeroAleatorio


print(Resultado)