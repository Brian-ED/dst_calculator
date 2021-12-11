import PySimpleGUI as sg
import math


# Character states:
charStates_dict = {"player":6, "ghost":3.6, "normal beefalo":7}

# some if statement to make sure you dont pick beef setting that i'm planning to add later.
characterMult_dict = {"WXOC" : 1.5, "WormwoodBloom" : 1.2 ,"WoodieB" : 1.1, "WoodieG" : 1.4, "WoodieM" : 0.9}

# Items
handItems_dict = {"thulicite club" : 1.1, "walking cane" : 1.25, "lazy explorer" : 1.25}
headItems_dict = {"ice cube", }
chestItem_dict = {"marble armor" : 0.7, "piggy back" : 0.9, "magiluminecense" : 1.2}

exoticMults_dict = {"road" : 1.3, "webbing" : 0.6, "antlion sinkhole" : 0.3, "honey trail" : 0.4, "sand storm" : 0.4}
    
# Layout

charStates_names = []
for a in charStates_dict.keys():
  charStates_names.append(a)

characterMult_names = []
for a in charStates_dict.keys():
  charStates_names.append(a)


layout = [
    [sg.Text('Choose your state:')],
    [sg.InputCombo(charStates_names,key="stateInput", enable_events=True, default_value="player")],
    [sg.Text("Choose your character:")],
    [sg.InputCombo(characterMult_names,key="stateInput")]
]


# TODO: the calculator of speedboosts
