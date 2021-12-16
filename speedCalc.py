import PySimpleGUI as sg
import pyperclip


# Character states:
charStates_dict = {"Player":6, "Ghost":3.6, "Default beefalo":7 ,"Ornery beefalo":7, "Rider beefalo":8, "Pudgy beefalo":6.5}

charMult_dict = {"Other characters" : 1, "WX-78 overcharge" : 1.5, "Wormwood bloom" : 1.2 ,"Woodie beaver" : 1.1, "Woodie goose" : 1.4, "Woodie moose" : 0.9}

# Items
handItems_dict = {"Empty":1,"Thulicite club" : 1.1, "Walking cane" : 1.25, "Lazy explorer" : 1.25}
headItems_dict = {"Empty":1, "Ice cube":0.9}
chestItems_dict = {"Empty":1, "Marble armor" : 0.7, "Piggy back" : 0.9, "Magiluminecense" : 1.2, "Sculpture":0.15}

exoticMults_dict = {"stormCheck":0.4,"roadCheck" : 1.3, "webbingCheck" : 0.6, "AntlionCheck" : 0.3, "honeyCheck" : 0.4}

saddles_dict = {"Default":1.4, "Glossomor":1.55, "WarSaddle":1.25}

exceptions_list = [["chestInput","Sculpture",0,1,0,1,1]]

# Layout

charStates_names = list(charStates_dict) # This is to get the keys
# vals = list(exoticMults_dict.values()) # This is to get the values

charMult_names = list(charMult_dict)
headItems_names = list(headItems_dict)
chestItems_names = list(chestItems_dict)
handItems_names = list(handItems_dict)
saddles_names  = list(saddles_dict)
exoticMults_names = list(exoticMults_dict)

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
    [sg.InputCombo(saddles_names, key="saddlesInput", default_value="Default", enable_events=True, disabled=True, visible=True)],


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


# Experiment where i simplify all the true and falses into one function:
def updateWindow(charInput, headInput, chestInput, handInput, saddlesInput):
    window["charInput"].update(disabled=bool(charInput))
    window["headInput"].update(disabled=bool(headInput))
    window["chestInput"].update(disabled=bool(chestInput))
    window["handInput"].update(disabled=bool(handInput))
    window["saddlesInput"].update(disabled=bool(saddlesInput))


while True:
    event, values = window.read()
    
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if values["stateInput"] == "Player":
        updateWindow(0,0,0,0,1)

        for i in range(0,len(exceptions_list)): # [["chestInput","Sculpture",0,0,0,0,1]]
            if values[exceptions_list[i][0]] == exceptions_list[i][1]:
                print(exceptions_list[i][2])
                updateWindow(exceptions_list[i][2],exceptions_list[i][3],exceptions_list[i][4],exceptions_list[i][5],exceptions_list[i][6])

        #if values["chestInput"] == "Sculpture":
        #    updateWindow(0,1,0,1,1)

    elif values["stateInput"] == "Default beefalo" or values['stateInput'] == "Ornery beefalo" or values['stateInput'] == "Rider beefalo" or values['stateInput'] == "Pudgy beefalo":
        updateWindow(1,1,1,1,0)
    
    elif values["stateInput"] == "Ghost":
        updateWindow(1,1,1,1,1)

    form = values['charInput']
    if form == "Woodie beaver" or form == "Woodie goose" or form == "Woodie moose":
        updateWindow(0,1,1,1,1)


    if event == 'Calculate':
        
        chest = chestItems_dict[values['chestInput']]
        character = charMult_dict[values["charInput"]]
        head = headItems_dict[values['headInput']]
        state = charStates_dict[values["stateInput"]]
        hand = handItems_dict[values['handInput']]

        if values['stateInput'] == "Player":
            if form == "Woodie beaver" or form == "Woodie goose" or form == "Woodie moose":
                speed = state * charMult_dict[values["charInput"]]
            elif values['chestInput'] == "Sculpture":
                speed = state*character*chest
            else: 
                speed = state * character * head * chest * hand

        elif values['stateInput'] == "Default beefalo" or values['stateInput'] == "Ornery beefalo" or values['stateInput'] == "Rider beefalo" or values['stateInput'] == "Pudgy beefalo": #"Player":6, "Ghost":3.6, "Default beefalo":7 ,"Ornery beefalo":7, "Rider beefalo":8, "Pudgy beefalo":6.5
            
            speed = saddles_dict[values["saddlesInput"]]*state

        elif values["stateInput"] == "Ghost":
            speed = charStates_dict[values["stateInput"]]

        if values["stateInput"] != "Ghost":
            
            if values['stateInput'] == "Default beefalo":
                for i in range(0, len(exoticMults_names)):
                    if values[exoticMults_names[i]]:
                        speed *= exoticMults_dict[exoticMults_names[i]]
            else:
                for i in range(0, len(exoticMults_names)):
                    if values[exoticMults_names[i]]:
                        speed *= exoticMults_dict[exoticMults_names[i]]


        window['output0'].update('You will get {0} speed.'.format(speed))

    if event == "Copy to clipboard":
        pyperclip.copy('{0}'.format(speed))


window.close()