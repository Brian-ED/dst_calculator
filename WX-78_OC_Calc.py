#from tkinter.constants import DISABLED # Looks like an unused import.
import PySimpleGUI as sg
import pyperclip
import random

# Layout

The_End_Is_Nigh_Picture = "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"
telelocatorStaff_Picture = "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"

layout = [

    [sg.Button("100%", image_data=The_End_Is_Nigh_Picture), sg.Button("20%", image_data=The_End_Is_Nigh_Picture), sg.Button(image_data=telelocatorStaff_Picture)],

    # Output text
    [sg.Text(size=(60,1), key='output0')],
    [sg.Text(size=(60,1), key='output1')],
    [sg.Text(size=(60,1), key='output2')],
    [sg.Text(size=(60,1), key='output3')],
    [sg.Text(size=(60,1), key='output4')],

    # Buttons
    [sg.Button("Exit"),sg.Button("Copy to clipboard"),sg.Button("Settings")]
]

window = sg.Window("DST Speed Calculator", layout)

bookUses100 = 0
bookUses20 = 0
staffUses = 0
totalStrikes = 0

mins = 0

settings_open = False

while True:

    event, values = window.read()

    if settings_open == False:
        if event == "Settings":
            settingsLayout = [

            [sg.Button("100%1"), sg.Button("20%1")],

            # Buttons
            [sg.Button("Exit")]
            ]
            settingsWindow = sg.Window("Settings menu", settingsLayout)
            settings_open = True


    if settings_open == True:
        settingsEvent, settingsValues = settingsWindow.read()

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if settingsEvent == sg.WINDOW_CLOSED or settingsEvent == 'Exit':
        settingsWindow.close()
        settings_open = False

    if event == "100%":
        bookUses100 += 1
        for _ in range(0,85):
            mins += ((24/(mins+24)) * 4) * (1+((random.random()*(24/(mins+24)))))
            totalStrikes += 1

    if event == "20%":
        bookUses20 += 1
        if bookUses20 == 5:
            bookUses100 += 1
            bookUses20 -= 5
        for _ in range(0,17):
            mins += ((24/(mins+24)) * 4) * (1+((random.random()*(24/(mins+24)))))
            totalStrikes += 1

    if event == "":
        staffUses += 1
        mins += ((24/(mins+24)) * 4) * (1+((random.random()*(24/(mins+24)))))
        totalStrikes += 1

    window['output0'].update('You will get {} minutes.'.format(mins))
    window['output1'].update('You have been striked {} times.'.format(totalStrikes))
    window['output2'].update('You have used staff {} times.'.format(staffUses))
    window['output3'].update("You have used {}% ".format(bookUses20*20) + "of a book extra.")
    window['output4'].update('You have used {} books.'.format(bookUses100))

    if event == "Copy to clipboard":
        pyperclip.copy('{0}'.format(mins))



window.close()