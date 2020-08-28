import math
"""
# Autor: Brito, A. E. S. C. / Bragança,C.
# Data: 19920102 / 20151001
# Objectivo: Calcular as raízes de uma equação do segundo grau.
#  No caso de não existirem raízes reais deve ser
#  enviada uma mensagem adequada.
# Variáveis:
# A --> Coeficiente de x2
# B --> Coeficiente de x
# C --> Coeficiente independente
# Delta --> Binómio discriminante
# X1, X2 --> Raízes da equação
"""

A = float(input("Coeficiente de x2: "))
B = float(input("Coeficiente de x: "))
C = float(input("Coeficiente independente: "))
if A == 0 :
    print(" a equação não é do segundo grau")
else:
    Delta =B * B - 4 * A * C


    if Delta > 0 :
        # Duas raízes reais e distintas
        X1 = ( - B + math.sqrt(Delta)) / (2 * A)
        X2 = ( - B - math.sqrt(Delta)) / (2 * A)
        print("Duas raízes reais: X1 = " + str(X1) + " X2 = " + str ( X2))
    elif Delta == 0:
        # Raíz real dupla
        X1 = - B / (2 * A)
        print("Raíz dupla X = " + str(X1))
    else:
         # Raízes imaginárias
        print("Não há raízes reais")
