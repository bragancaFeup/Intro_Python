
""""
Autor: Bragança / Brito, A. E. S. C.
Data: 2019

# Dado um texto determinar o número de vezes que aparece cada uma das diferentes palavras.
# Admite-se que as palavras se encontram separadas por um espaço em branco.

"""
Npalavras = 0

Frase = input(" Frase")


Frase = Frase.strip() + " "  # adicionar um espaço no fim da frase para tratar a ultima palavra como as restantes
LenFrase = len(Frase)

InicioPalavra = 0               # a primeira palavra inicia na posição 0 da frase

Palavras=Frase.split()
Npalavras = len(Palavras)

print(f"Frase com  {Npalavras} Palavras")
print(Palavras)

for K in range(len(Palavras)):  #Percorre todas as palavras
    # contar quantas vezes já apareceu a palavra s   d d  d s d
    NumeroRepeticoes = 0
    for J in range(0, K + 1):
        if Palavras[J] == Palavras[K]:
            NumeroRepeticoes = NumeroRepeticoes + 1

    if NumeroRepeticoes == 1:  # se entre 0 e K só apareceu uma vez significa que é uma nova palavra
        # conta as repetiçoes até ao fim da frase
        NumeroRepeticoes = 0
        for J in range(K, Npalavras ):
            if Palavras[J] == Palavras[K]:
                NumeroRepeticoes = NumeroRepeticoes + 1

        print(f"A palavra {Palavras[K]}  repete-se  {NumeroRepeticoes} vezes")
