import PySimpleGUI as sg

def myPoppup():
    sg.Popup('bbb','cc',title="aaaaaaaaaaaaaaaaa",button_color=('white', 'red'))
    # sg.Popup('Popup')  # Shows OK button
    #sg.PopupOk('PopupOk')  # Shows OK button
    #sg.PopupYesNo('PopupYesNo')  # Shows Yes and No buttons
    #sg.PopupCancel('PopupCancel')  # Shows Cancelled button
    #sg.PopupOKCancel('PopupOKCancel')  # Shows OK and Cancel buttons

    # sg.PopupError('PopupError')  # Shows red error button
    # sg.PopupTimed('PopupTimed')  # Automatically closes
    # sg.PopupAutoClose('PopupAutoClose')  # Same as PopupTimed