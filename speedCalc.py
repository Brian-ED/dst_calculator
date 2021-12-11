import PySimpleGUI as sg
import math


# Character states:
charStates_dict = {"player":6, "ghost":3.6, "normal beefalo":7}

# some if statement to make sure you dont pick beef setting that i'm planning to add later.
charMult_dict = {"Other characters" : 1, "WXOC" : 1.5, "WormwoodBloom" : 1.2 ,"WoodieB" : 1.1, "WoodieG" : 1.4, "WoodieM" : 0.9}

# Items
handItems_dict = {"Empty":1,"thulicite club" : 1.1, "walking cane" : 1.25, "lazy explorer" : 1.25}
headItems_dict = {"Empty":1, "ice cube":0.9}
chestItems_dict = {"Empty":1, "marble armor" : 0.7, "piggy back" : 0.9, "magiluminecense" : 1.2}

exoticMults_dict = {"road" : 1.3, "webbing" : 0.6, "antlion sinkhole" : 0.3, "honey trail" : 0.4, "sand storm" : 0.4}
    
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

layout = [
    # Character state : in other words, dead, alive, or is a beefalo
    [sg.Text('Choose your state:')],
    [sg.InputCombo(charStates_names,key="stateInput", enable_events=True, default_value="player")],

    # Character buff
    [sg.Text("Choose your character:")],
    [sg.InputCombo(charMult_names, key="charInput", default_value="Other characters", enable_events=True)],

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

    # Buttons
    [sg.Button('Calculate'), sg.Button('Exit')]
]

window = sg.Window('DST Speed Calculator', layout)


# TODO: the calculator of speedboosts

while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'Calculate':
        state = charStates_dict[values['stateInput']]
        character = charMult_dict[values["charInput"]]
        head = headItems_dict[values['headInput']]
        chest = chestItems_dict[values['chestInput']]
        hand = handItems_dict[values['handInput']]
        speed = state * character * head * hand * hand
        window['output0'].update('You will get {0} speed.'.format(speed))


# Finish up by removing from the screen
window.close()