"""
'Autor: Bragança
'Data: 2009
'6.2 Escreva um programa em VBASIC que dados os nomes de três ficheiros,
'de acesso sequencial, copie o conteúdo dos dois primeiros para o terceiro
'Variáveis:
 Fiche1 Nome Ficheiro1
 Fiche2 Nome Ficheiro2
 Fiche3 Nome Ficheiro2
 linha
"""

Fiche1 = "Ficheiro1.txt"
Fiche2 = "Ficheiro2.txt"
Fiche3 = "Ficheiro3.txt"

f1 = open(Fiche1,"r")
f2 = open(Fiche2,"r")
f3 = open(Fiche3,"w")

for Linha in f1:
    f3.write(Linha)

for Linha in f2:
    f3.write(Linha)

f1.close()
f2.close()
f3.close()
