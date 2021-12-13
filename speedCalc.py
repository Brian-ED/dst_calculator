#from tkinter.constants import DISABLED # Looks like an unused import.
import PySimpleGUI as sg
import pyperclip

speed = ""

# Character states:
charStates_dict = {"Player":6, "Ghost":3.6, "Default beefalo":7 ,"Ornery beefalo":7, "Rider beefalo":8, "Pudgy beefalo":6.5}

# some if statement to make sure you dont pick beef setting that i'm planning to add later.
charMult_dict = {"Other characters" : 1, "WX-78 overcharge" : 1.5, "Wormwood bloom" : 1.2 ,"Woodie beaver" : 1.1, "Woodie goose" : 1.4, "Woodie moose" : 0.9}

# Items
handItems_dict = {"Empty":1,"Thulicite club" : 1.1, "Walking cane" : 1.25, "Lazy explorer" : 1.25}
headItems_dict = {"Empty":1, "Ice cube":0.9}
chestItems_dict = {"Empty":1, "Marble armor" : 0.7, "Piggy back" : 0.9, "Magiluminecense" : 1.2}

exoticMults_dict = {"stormCheck":0.4,"roadCheck" : 1.3, "webbingCheck" : 0.6, "AntlionCheck" : 0.3, "honeyCheck" : 0.4}

saddles_dict = {"Default":1.4, "Glossomor":1.55, "WarSaddle":1.25}
    
# Layout


def DictToList(dictionary, list):
    for a in dictionary.keys():
        list.append(a)

charStates_names = []
DictToList(charStates_dict,charStates_names)

charMult_names = []
DictToList(charMult_dict,charMult_names)

headItems_names = []
DictToList(headItems_dict,headItems_names)

chestItems_names = []
DictToList(chestItems_dict,chestItems_names)

handItems_names = []
DictToList(handItems_dict,handItems_names)

saddles_names = []
DictToList(saddles_dict, saddles_names)

exoticMults_names = []
DictToList(exoticMults_dict,exoticMults_names)

layout = [
    # Character state : in other words, dead, alive, or is a beefalo
    [sg.Text('Choose your state:')],
    [sg.InputCombo(charStates_names,key="stateInput", enable_events=True, default_value="Player")],

    # Character buff
    [sg.Text("Choose your character:")],
    [sg.InputCombo(charMult_names, key="charInput", default_value="Other characters", enable_events=True, disabled=False, visible=True)],

    # Head slot
    [sg.Text("Choose your head item:")],
    [sg.InputCombo(headItems_names, key="headInput", default_value="Empty", enable_events=True, disabled=False, visible=True)],

    # Chest items
    [sg.Text("Choose your chest item:")],
    [sg.InputCombo(chestItems_names, key="chestInput", default_value="Empty", enable_events=True, disabled=False, visible=True)],

    # Hand slot
    [sg.Text("Choose your hand item:")],
    [sg.InputCombo(handItems_names, key="handInput", default_value="Empty", enable_events=True, disabled=False, visible=True)],

    # Saddle

    [sg.Text("Choose your saddle")],
    [sg.InputCombo(saddles_names, key="saddlesInput", default_value="Default", enable_events=True, disabled=True)],


    # Checkboxes
    [sg.Checkbox("Storm",key="stormCheck"),
    sg.Checkbox("Road",key="roadCheck"),
    sg.Checkbox("Webbing",key="webbingCheck"),
    sg.Checkbox("Antlion sinkhole",key="AntlionCheck"),
    sg.Checkbox("Honey trail",key="honeyCheck")],

    # Output text
    [sg.Text(size=(60,1), key='output0')],

    # Buttons
    [sg.Button("Calculate"), sg.Button("Exit"),sg.Button("Copy to clipboard")]
]

window = sg.Window("DST Speed Calculator", layout)

while True:
    event, values = window.read()
    
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if values['stateInput'] == "Player":
        window['charInput'].update(disabled=False)
        window['headInput'].update(disabled=False)
        window['chestInput'].update(disabled=False)
        window["handInput"].update(disabled=False)
        window['headInput'].update(disabled=False)
        window['saddlesInput'].update(disabled=True)

    elif values['stateInput'] == "Default beefalo" or values['stateInput'] == "Ornery beefalo" or values['stateInput'] == "Rider beefalo" or values['stateInput'] == "Pudgy beefalo":
        window['charInput'].update(disabled=True)
        window['headInput'].update(disabled=True)
        window['chestInput'].update(disabled=True)
        window["handInput"].update(disabled=True)
        window['headInput'].update(disabled=True)
        window['saddlesInput'].update(disabled=False)
    
    elif values["stateInput"] == "Ghost":
        window['charInput'].update(disabled=True)
        window['headInput'].update(disabled=True)
        window['chestInput'].update(disabled=True)
        window["handInput"].update(disabled=True)
        window['headInput'].update(disabled=True)
        window['saddlesInput'].update(disabled=True)


    if event == 'Calculate':

        # TODO: beefalo saddles.

        state = charStates_dict[values["stateInput"]]
        if values['stateInput'] == "Player":

            character = charMult_dict[values["charInput"]]
            head = headItems_dict[values['headInput']]
            chest = chestItems_dict[values['chestInput']]
            hand = handItems_dict[values['handInput']]
            speed = state * character * head * chest * hand

        elif values['stateInput'] == "Default beefalo" or values['stateInput'] == "Ornery beefalo" or values['stateInput'] == "Rider beefalo" or values['stateInput'] == "Pudgy beefalo": #"Player":6, "Ghost":3.6, "Default beefalo":7 ,"Ornery beefalo":7, "Rider beefalo":8, "Pudgy beefalo":6.5
            
            speed = saddles_dict[values["saddlesInput"]]*charStates_dict[values["stateInput"]]

        elif values["stateInput"] == "Ghost":
            speed = charStates_dict[values["stateInput"]]

        if values["stateInput"] != "Ghost":
            for i in range(0, len(exoticMults_names)):
                if values[exoticMults_names[i]]:
                    speed *= exoticMults_dict[exoticMults_names[i]]


        window['output0'].update('You will get {0} speed.'.format(speed))

    if event == "Copy to clipboard":
        pyperclip.copy('{0}'.format(speed))


# Finish up by removing from the screen
window.close()