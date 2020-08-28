"""
'Autor: Bragança
'Data: 2009
'6.3 Considere dois ficheiros de acesso sequencial tendo cada um armazenado uma lista de valores. Escreva um
programa em VBASIC que construa um terceiro ficheiro de acesso sequencial contendo a média aritmética
dos dois valores correspondentes dos dois ficheiros.
(Nota: não deverá utilizar variáveis indexadas)
'Variáveis:
 Fiche1 Nome Ficheiro1
 Fiche2 Nome Ficheiro2
 Fiche3 Nome Ficheiro2
 linha
"""
import os   #     The os module in Python provides a way of using operating system dependent functionality.

Fiche1 = "Ficheiro1.txt"
Fiche2 = "Ficheiro2.txt"
Fiche3 = "Ficheiro3.txt"

if os.path.exists(Fiche1) and os.path.exists(Fiche2):
    f1 = open(Fiche1,"r")
    f2 = open(Fiche2, "r")
    f3 = open(Fiche3,"w")

    while



    f3.close()
    f2.close()
    f1.close()
