""""
Autor: Bragança / Brito, A. E. S. C.
Data: 2019
# Objectivo: Dado um vetor de dimensão N determinar o número que aparece mais         vezes
# bem como as posições na lista, onde ele aparece

# Variáveis:
#         Dim N As Integer # Número de valores da lista
#         Dim Lista[100] As Single
#         Dim NumeroRepetido As Single #Número que mais vezes é repetido
#         Dim NumeroRepeticoes As Integer = 0 #Número máximo de repetições
#         Dim NumeroRepeticoesTemporario As Integer = 0
#         Dim K As Integer # Contador
#         Dim I As Integer # Contador para o segundo ciclo

"""
NumeroRepeticoes =0
NumeroRepeticoesTemporario=0
N = int(input("Por favor insira N"))

Lista=[None]*N
K = 0

while K < N:  # Ciclo que armazena a lista inserida:
    Lista[K] = int(input("Por favor insira o próximo valor da lista"))
    K = K + 1

K = 0
while K < N - 1:      # Ciclo que vai percorrer todos os elementos da lista:
    NumeroRepeticoesTemporario = 0
    I = K
    while I < N:      # Ciclo que, para cada elemento da lista, vai calcular o nº de repetiçoes:
        if Lista[I] == Lista[K]:
            NumeroRepeticoesTemporario = NumeroRepeticoesTemporario + 1
        I = I + 1
    if NumeroRepeticoesTemporario > NumeroRepeticoes:
        NumeroRepeticoes = NumeroRepeticoesTemporario
        NumeroRepetido = Lista[K]
    K = K + 1

print("O Valor que mais se repetiu foi o " , NumeroRepetido , ". Repetiu-se " , NumeroRepeticoes , " vezes.")
print("As posições em que se repetiu foram: ")
K = 0
while K < N:
    if Lista[K] == NumeroRepetido:
        print(" A " , K , " Posicao")
    K = K + 1


