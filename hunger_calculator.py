# TODO: calculation of how much hunger you need for X days and how many days X amount of X dish will keep you fed

import PySimpleGUI as sg
from pyperclip import copy as copy_to_cb

headItems_dict = {"funcaps":25} # Add slurper and check hunger drain in code
chestItems_dict = {"Belt of hunger":0.6, "Hibearnation vest":0.75}

# Layout

layout = [

        [sg.Input(key='Hunger', default_text="150")],
        
        # Output text
        [sg.Text(size=(60,1), key='output0')],
        
        # Buttons
        [sg.Button("Exit"),sg.Button("Copy to clipboard")]
    ]

window = sg.Window("DST Speed Calculator", layout)

timeUntilStarvation = "some formula" # TODO add the actual hunger formula that i can't seem to find

while True:

    event, values = window.read()

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == "Copy to clipboard":
        copy_to_cb('{0}'.format(timeUntilStarvation))

window.close()