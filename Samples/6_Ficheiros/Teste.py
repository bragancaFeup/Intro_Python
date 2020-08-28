# import PySimpleGUI as sg
#
# event, values = sg.Window('Get filename example', [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).Read()
#
# print(event)
# print(values)
#
# print (values[0])

import myPySimpleGUI.MyGUI as myIO


myIO.myPoppup()