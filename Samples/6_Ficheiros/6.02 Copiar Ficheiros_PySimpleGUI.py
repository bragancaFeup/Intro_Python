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

import PySimpleGUI as sg


def go(Fiche1,Fiche2,Fiche3):

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

    print ("fim")




sg.change_look_and_feel('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Text('File 1'), sg.InputText(), sg.FileBrowse()
     ],
    [sg.Text('File 2'), sg.InputText(), sg.FileBrowse()
     ],
    [sg.Text('File 2'), sg.InputText(), sg.FileBrowse()
     ],
    [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Cancel()]
]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    #print('You entered ', values)
    go(values[0],values[1],values[2])
window.close()



