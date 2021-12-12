#from tkinter.constants import DISABLED # Looks like an unused import.
import PySimpleGUI as sg
import pyperclip

speed = ""

# Character states:
charStates_dict = {"player":6, "ghost":3.6, "normal beefalo":7}

# some if statement to make sure you dont pick beef setting that i'm planning to add later.
charMult_dict = {"Other characters" : 1, "WX-78 overcharge" : 1.5, "Wormwood bloom" : 1.2 ,"Woodie beaver" : 1.1, "Woodie goose" : 1.4, "Woodie moose" : 0.9}
beef_dict = {"Default":1 ,"Ornery":1, "Rider":1.14285714286, "Pudgy":6.5}

# Items
handItems_dict = {"Empty":1,"Thulicite club" : 1.1, "Walking cane" : 1.25, "Lazy explorer" : 1.25}
headItems_dict = {"Empty":1, "Ice cube":0.9}
chestItems_dict = {"Empty":1, "Marble armor" : 0.7, "Piggy back" : 0.9, "Magiluminecense" : 1.2}

exoticMults_dict = {"Road" : 1.3, "Webbing" : 0.6, "Antlion sinkhole" : 0.3, "Honey trail" : 0.4}
    
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

beefDict_names = []
DictToList(beef_dict, beefDict_names)

layout = [
    # Character state : in other words, dead, alive, or is a beefalo
    [sg.Text('Choose your state:')],
    [sg.InputCombo(charStates_names,key="stateInput", enable_events=True, default_value="player")],

    # Character buff
    [sg.Text("Choose your character:")],
    [sg.InputCombo(charMult_names, key="charInput", visible=True, default_value="Other characters", enable_events=True)],

    # Beefalo trait
    [sg.InputCombo(beefDict_names, key="beefInput", visible=False, default_value="Default", enable_events=True)],

    # Head slot
    [sg.Text("Choose your head item:")],
    [sg.InputCombo(headItems_names, key="headInput", default_value="Empty", enable_events=True)],

    # Chest items
    [sg.Text("Choose your chest item:")],
    [sg.InputCombo(chestItems_names, key="chestInput", default_value="Empty", enable_events=True)],

    # Hand slot
    [sg.Text("Choose your hand item:")],
    [sg.InputCombo(handItems_names, key="handInput", default_value="Empty", enable_events=True)],

    # Output text
    [sg.Text(size=(60,1), key='output0')],

    # Checkboxes
    [sg.Checkbox("Storm",key="stormCheck")], # {"Road" : 1.3, "Webbing" : 0.6, "Antlion sinkhole" : 0.3, "Honey trail" : 0.4}
    [sg.Checkbox("Road",key="roadCheck")],
    [sg.Checkbox("Webbing",key="webbingCheck")],
    [sg.Checkbox("Antlion sinkhole",key="AntlionCheck")],
    [sg.Checkbox("Honey trail",key="stormInput")],

    # Buttons
    [sg.Button("Calculate"), sg.Button("Exit"),sg.Button("Copy to clipboard")]
]

window = sg.Window("DST Speed Calculator", layout)

while True:
    event, values = window.read()
    
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if values["stateInput"] != "player":
        window['charInput'].update(visible=False)
    else: window['charInput'].update(visible=True)

    if values["stateInput"] != "normal beefalo":
        window["beefInput"].update(visible=False)
    else: window['beefInput'].update(visible=True)


    if event == 'Calculate':

        # Fixed a bit of code here, because stateInput in state was running through dict and turned from "player" into 6
        # and was unable to be checked correctly. TODO: beefalo saddles.

        state = charStates_dict[values["stateInput"]]
        if values['stateInput'] == "player":
            character = charMult_dict[values["charInput"]]
            head = headItems_dict[values['headInput']]
            chest = chestItems_dict[values['chestInput']]
            hand = handItems_dict[values['handInput']]

        speed = state * character * head * hand

        # Not sure why you used "for in" here, the "i" seems like it's unused anyway, so I removed that.

        if values["stormCheck"]:
            speed *= 0.4

        if values["roadCheck"]:
            speed *= 1.3
        

        window['output0'].update('You will get {0} speed.'.format(speed))

    if event == "Copy to clipboard":
        pyperclip.copy('{0}'.format(speed))


# Finish up by removing from the screen
window.close()