"""
# Autor: Bragança
# Data: 2007/11/14
# Objectivo: Determinar os números ímpares sucessivos cuja
# soma seja igual a N3 quando N
# assume valores entre 1 e 20.
# (ex: 1^3 = 1 ; 2^3 = 3 + 5 ; 3^3 = 7 + 9 + 11)
# Variáveis:
Dim SomImp As Integer # Soma dos números ímpares sucessivos
Dim Resultado As String #  String com o resultado
Dim N As Integer = 20
Dim I As Integer
Dim J As Integer
Dim K As Integer
Dim L As Integer
Dim Cubo As Integer
Dim LimiteSupImp As Integer

"""
N = 20

for I in range(1, N + 1):
    Cubo = I ** 3
    LimiteSupImp = int(Cubo / 2 + 2)
    for J in range(1, LimiteSupImp + 1, 2):
        SomImp = J
        for K in range(J + 2, LimiteSupImp + 1, 2):
            SomImp = SomImp + K
            if Cubo == SomImp:
                Resultado = ""
                for L in range(J, K + 1, 2):
                    Resultado = Resultado + " + " + str(L)
                print(str(I) + "^3 = " + str(Cubo) + "->" + Resultado)
