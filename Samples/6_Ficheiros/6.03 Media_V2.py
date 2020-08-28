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
import PySimpleGUI as sg
cwd = os.getcwd()

Fiche1 = sg.PopupGetFile("Escolha ficheiro 1",default_path=cwd)
Fiche2 = sg.PopupGetFile("Escolha ficheiro 2",default_path=cwd)
Fiche3 = sg.PopupGetFile("Escolha ficheiro 3",default_path=cwd)


if os.path.exists(Fiche1):
    f1 = open(Fiche1,"r")
    a=f1.read()
    print(a)
    b = f1.read()
    print(b)
    if os.path.exists(Fiche2):
        f2 = open(Fiche2,"r")

        f3 = open(Fiche3,"w")

        for Linha in f1:
            f3.write(Linha)

        for Linha in f2:
            f3.write(Linha)

        f3.close()
        f2.close()
    f1.close()
