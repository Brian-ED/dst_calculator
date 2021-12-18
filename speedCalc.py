import PySimpleGUI as sg
from pyperclip import copy as copy_to_cb


# Character states:
charStates_dict = {"Player":6, "Ghost":3.6, "Default beefalo":7 ,"Ornery beefalo":7, "Rider beefalo":8, "Pudgy beefalo":6.5}

charMult_dict = {"Other characters" : 1, "WX-78 overcharge" : 1.5, "Wormwood bloom" : 1.2 ,"Woodie beaver" : 1.1, "Woodie goose" : 1.4, "Woodie moose" : 0.9}

# Items
handItems_dict = {"Empty":1,"Thulicite club" : 1.1, "Walking cane" : 1.25, "Lazy explorer" : 1.25}
headItems_dict = {"Empty":1, "Ice cube":0.9}
chestItems_dict = {"Empty":1, "Marble armor" : 0.7, "Piggy back" : 0.9, "Magiluminecense" : 1.2, "Sculpture":0.15}

exoticMults_dict = {"stormCheck":0.4,"roadCheck" : 1.3, "webbingCheck" : 0.6, "AntlionCheck" : 0.3, "honeyCheck" : 0.4}

saddles_dict = {"Default":1.4, "Glossomor":1.55, "WarSaddle":1.25}

# the six didgets in order mean if the following should be disabled: state, character, head, chest, hand, saddle.
# 0 means they shall not be touched, 1 means they should be off.

exceptions_list=[["stateInput","Player"         ,0,0,0,0,0,1],
                ["chestInput","Sculpture"       ,0,0,1,0,1,1],
                ["charInput","Woodie beaver"    ,0,0,1,1,1,1],
                ["charInput","Woodie goose"     ,0,0,1,1,1,1],
                ["charInput","Woodie moose"     ,0,0,1,1,1,1],
                ["stateInput", "Ghost"          ,0,1,1,1,1,1],
                ["stateInput", "Default beefalo",0,1,1,1,1,0],
                ["stateInput", "Ornery beefalo" ,0,1,1,1,1,0],
                ["stateInput", "Rider beefalo"  ,0,1,1,1,1,0],
                ["stateInput", "Pudgy beefalo"  ,0,1,1,1,1,0]]

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
    [sg.Text("Choose your state:")],
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
    [sg.Text(size=(60,1), key="output0")],

    # Buttons
    [sg.Button("Calculate"), sg.Button("Exit"),sg.Button("Copy to clipboard",disabled=True)]
]

window = sg.Window("DST Speed Calculator", layout)


# i simplify all the true and falses into one function:
def updateWindow(stateInput, charInput, headInput, chestInput, handInput, saddlesInput):
    window["stateInput"].update(disabled=bool(stateInput))
    window["charInput"].update(disabled=bool(charInput))
    window["headInput"].update(disabled=bool(headInput))
    window["chestInput"].update(disabled=bool(chestInput))
    window["handInput"].update(disabled=bool(handInput))
    window["saddlesInput"].update(disabled=bool(saddlesInput))

while True:
    event, values = window.read()
    
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    for i in range(0,len(exceptions_list)):
        if values[exceptions_list[i][0]] == exceptions_list[i][1]:
            updateWindow(exceptions_list[i][2],exceptions_list[i][3],exceptions_list[i][4],exceptions_list[i][5],exceptions_list[i][6],exceptions_list[i][7])

    # When the calculate button has been hit, it will calculate all the multipliers selected.

    if event == "Calculate":
        
        state = charStates_dict[values["stateInput"]]
        character = charMult_dict[values["charInput"]]
        head = headItems_dict[values["headInput"]]
        chest = chestItems_dict[values["chestInput"]]
        hand = handItems_dict[values["handInput"]]
        saddles = saddles_dict[values["saddlesInput"]]

        prevState, prevchar, prevhead, prevchest, prevhand, prevsaddle = 0, 0, 0, 0, 0, 0
        
        for i in range(0,len(exceptions_list)):
            if values[exceptions_list[i][0]] == exceptions_list[i][1]:
                prevState = prevState or 0**exceptions_list[i][2]
                prevchar = prevchar or 0**exceptions_list[i][3]
                prevhead = prevhead or 0**exceptions_list[i][4]
                prevchest = prevchest or 0**exceptions_list[i][5]
                prevhand = prevhand or 0**exceptions_list[i][6]
                prevsaddle = prevsaddle or 0**exceptions_list[i][7]

        speed = (state**prevState) * (character**prevchar) * (head**prevhead) * (chest**prevchest) * (hand**prevhand) * (saddles**prevsaddle)

        # Adds on all the extra speedbuffs, like road, storm, etc. 
                 
        for i in range(0, len(exoticMults_names)):
            if values[exoticMults_names[i]]:
                if values["stateInput"] == "Default beefalo" or values["stateInput"] == "Ornery beefalo" or \
                   values["stateInput"] == "Rider beefalo" or values["stateInput"] == "Pudgy beefalo":
                    if exoticMults_names[i] != "roadCheck" and exoticMults_names[i] != "stormCheck":
                        speed *= exoticMults_dict[exoticMults_names[i]]
                        print(speed)
                else:
                    speed *= exoticMults_dict[exoticMults_names[i]]

        window["output0"].update("You will get {0} speed.".format(speed))

        window['Copy to clipboard'].update(disabled=False)

    if event == "Copy to clipboard":
        copy_to_cb("{0}".format(speed))


window.close()