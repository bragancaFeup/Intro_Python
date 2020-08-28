"""
# Autor: Bragança
# Data: 2019
# Determina se um número é primo utilizando a instrução - While
Dim N As Integer # Valor dado
Dim I As Integer # Divisores de N


"""

N = int(input("Valor:"))

I = 2
while I <= N / 2 and N % I != 0:  # Enquanto I não for divisor de N
    I = I + 1

if I > N / 2:  # Se não tem divisores além de 1 e dele próprio
    print(" {} é primo".format(N))
else:
    print(" {} Não é primo".format(N))
