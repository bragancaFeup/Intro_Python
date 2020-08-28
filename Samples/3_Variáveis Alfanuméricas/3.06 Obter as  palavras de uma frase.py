""""
Autor: Bragança / Brito, A. E. S. C.
Data: 2019

# Obter as  palavras de uma frase

"""
Npalavras = 0

Frase = input(" Frase")


Frase = Frase.strip() + " "  # adicionar um espaço no fim da frase para tratar a ultima palavra como as restantes
LenFrase = len(Frase)

InicioPalavra = 0               # a primeira palavra inicia na posição 0 da frase

Palavras=[]                     # Cria Vetor para armazenar as palavras
for K in range(0, LenFrase ):
    if Frase[K] == " ":                     # procurar os espaços
        Npalavras = Npalavras + 1           # encontrado um espaço temos mais uma palavra
        Palavra = Frase[InicioPalavra: K]   # obtem a palavra desde a posição InicioPalavra (inclusive) até K (exclusive)
        Palavras.append(Palavra)            # Adiciona à lista de palavras
        InicioPalavra = K + 1               # a proxima palavra inicia na posição a seguir ao espaço

print(f"Frase com  {Npalavras} Palavras")
print(Palavras)