import PySimpleGUI as sg
import math

# Character states:
charStates = {"player":6, "ghost":3.6}

# some if statement to make sure you dont pick beef setting that i'm planning to add later.
# slider for wolfgang hunger 0.9-1.25 speed mult according to wiki
characterMult = {"WXOC" : 1.5, "WormwoodBloom" : 1.2 ,"WoodieB" : 1.1, "WoodieG" : 1.4, "WoodieM" : 0.9}

# Items
handItems = {"thulicite club":1.1, "walking cane":1.25, "lazy explorer":1.25, "magiluminecense":1.2}
headItems = {"ice cube", }
chestItem = {"marble armor": 1, "piggy back":0.9}

exoticMults = {"road" : 1.3, "webbing":0.6, "antlion sinkhole": 0.3, "honey trail":0.4, "sand storm":0.4}
