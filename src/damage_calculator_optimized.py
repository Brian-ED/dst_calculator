import PySimpleGUI as sg
import math
import copy
from pyperclip import copy as copy_to_cb
damage_dict = {"Dark Sword": 68, "Glass Cutter": 68, "Glass Cutter (attacking a shadow)": 68,
               "Thulecite Club": 59.5, "Ham Bat": 59.5, "Weremoose": 59.5, "Tentacle Spike": 51,
               "Bat Bat": 42.5, "Battle Spear": 42.5, "Spear": 34, "Morning Star": 28.9,
               "Tail o' Three Cats": 27.2, "Boomerang": 27.2, "Strident Trident (spell attack)": 85,
               "Strident Trident (on a boat)": 68, "Strident Trident (on land)": 27.2, "Werebeaver": 27.2,
               "Werebeaver (attacking treeguards)": 44.2, "Electric Dart": 60, "Blow Dart": 100,
               "Trusty Slingshot": 0, "Alarming Clock" : 81.6 }

durability_dict = {"Dark Sword": 100, "Glass Cutter": 75, "Glass Cutter (attacking a shadow)": 150,
                   "Thulecite Club": 200, "Ham Bat": 0, "Weremoose": 0, "Tentacle Spike": 100,
                   "Bat Bat": 75, "Battle Spear": 200, "Spear": 150, "Morning Star": 720,
                   "Tail o' Three Cats": 150, "Boomerang": 10, "Strident Trident (spell attack)": 25,
                   "Strident Trident (on a boat)": 150, "Strident Trident (on land)": 150, "Werebeaver": 0,
                   "Werebeaver (attacking treeguards)": 0, "Electric Dart": 1, "Blow Dart": 1,
                   "Trusty Slingshot" : 1, "Alarming Clock" : 96 }
character_dict = {"Wolfgang (mighty)": 2, "Wigfrid": 1.25, "Wendy": 0.75, "Wes" : 0.75, "Other characters": 1}
wanda_dict = { "Young" : 1, "Middle-aged" : 1.2, "Old" : 1.75, "I am not Wanda" : 1 }
walter_dict = { "Rocks" : 17, "Golden rounds" : 34, "Marbles" : 51, "Slowing down rounds" : 17, "Cursed rounds" : 51,
                "Trinket" : 59.5 }
damage_dict_keys = []
for i in damage_dict.keys():
    damage_dict_keys.append(i)
character_dict_keys = []
for i in character_dict.keys():
    character_dict_keys.append(i)
wanda_dict_keys = []
for i in wanda_dict.keys():
    wanda_dict_keys.append(i)
wanda_dict_keys_2 = copy.copy(wanda_dict_keys)
wanda_dict_keys.remove("I am not Wanda")
walter_dict_keys = []
for i in walter_dict.keys():
    walter_dict_keys.append(i)
layout = [
    [sg.Text('Choose your weapon:')],
    [sg.InputCombo(damage_dict_keys, key='weaponinput', enable_events=True, default_value="Spear")],
    [sg.Text("Middle-length text, so nothing will shrink:", key="spectext", visible=False)],
    [sg.InputCombo(("Just some text so", " it won't shrink"), key="specinput", visible=False)],
    [sg.Text('Choose your character:')],
    [sg.InputCombo(character_dict_keys, size=(20, 1), key='characterinput', default_value="Other characters",
                   enable_events=True)],
    [sg.Text('Choose damage buffs:')],
    [sg.Checkbox('', key='chiliinput'), sg.Text('Chili Spice'),
     sg.Checkbox('', key='electricinput'), sg.Text('Volt Goat Chaud Froid'),
     sg.Checkbox('', key='wetinput'), sg.Text('Target is Wet')],
     [sg.Checkbox('', key='cccrowninput'), sg.Text('Enlightened Crown is Equipped'),
     sg.Checkbox('', key='abigailinput'), sg.Text('Target is attacked by Abigail')],
    [sg.Text('Choose durability buffs:')],
    [sg.Checkbox('', key='warbleinput'), sg.Text('Weaponized Warble')],
    [sg.Text("Write your enemy's health:")],
    [sg.Input(key='healthinput', default_text="16000")],
    [sg.Text(size=(60,1), key='output0')],
    [sg.Text(size=(60,1), key='output1')],
    [sg.Text(size=(60,1), key='output2')],
    [sg.Text(size=(60,1), key='output3')],
    [sg.Button('Calculate'), sg.Button('Exit'), sg.Button("Copy to clipboard", disabled=True)]]

window = sg.Window('DST Damage Calculator', layout)

while True:
    event, values = window.read()
    if values['weaponinput'][0:4] == "Were":
        window['cccrowninput'].update(disabled=True)
        values['cccrowninput'] = False
    if values['weaponinput'][0:4] != "Were":
        window['cccrowninput'].update(disabled=False)
    if values['weaponinput'][0:6] == "Trusty" or values['weaponinput'][0:4] == "Were" or values['weaponinput'][0:8] == "Alarming":
        window['characterinput'].update(value="Other characters", disabled=True)
        values['characterinput'] = "Other characters"
    if values['weaponinput'][0:6] != "Trusty" and values['weaponinput'][0:8] != "Alarming":
        result = False
        if values['weaponinput'][0:4] == "Dark" and values['characterinput'] == "Other characters":
            result = True
        if values['weaponinput'][0:4] != "Were":
            window['characterinput'].update(disabled=False)
        if not result:
            window['spectext'].update(visible=False)
            window['specinput'].update(visible=False)
    if values['weaponinput'] == "Morning Star" or values['weaponinput'] == "Electric Dart":
        window['electricinput'].update(disabled=True)
        values['electricinput'] = True
    if values['weaponinput'] != "Morning Star" and values['weaponinput'] != "Electric Dart":
        window['electricinput'].update(disabled=False)
    if values['weaponinput'][0:8] == "Alarming":
        window['spectext'].update("Choose your age:", visible=True)
        window['specinput'].update(values=(wanda_dict_keys), visible=True)
    if values['weaponinput'][0:4] == "Dark" and values['characterinput'] == "Other characters":
        window['spectext'].update("Choose your age:", visible=True)
        window['specinput'].update(values=(wanda_dict_keys_2), visible=True)
    if values['weaponinput'][0:6] == "Trusty":
        window['spectext'].update("Choose your ammos:", visible=True)
        window['specinput'].update(values=(walter_dict_keys), visible=True)
    window['spectext'].update()
    window['specinput'].update()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'Calculate':
        damage = float(damage_dict[values['weaponinput']] * character_dict[values['characterinput']])
        if values['weaponinput'][0:8] == "Alarming" or (values['weaponinput'][0:4] == "Dark" and values['characterinput'] == "Other characters"):
            damage *= wanda_dict[values['specinput']]
        if values['weaponinput'][0:6] == "Trusty":
            damage += walter_dict[values['specinput']]
        durability = int(durability_dict[values['weaponinput']])
        values['healthinput'] = int(values['healthinput'])
        if values['abigailinput']:
            damage *= 1.1
            if values['characterinput'] == "Wendy":
                damage *= 1.4
        if values['chiliinput']:
            damage *= 1.2
        if values['electricinput']:
            if values['wetinput']:
                damage *= 2.5
            else:
                damage *= 1.5
        hits = values['healthinput'] / damage
        if values['warbleinput']:
            if durability > 1:
                durability *= 1.25
        weapons = values['healthinput'] / damage / durability
        if values['cccrowninput']:
            damage += 42.5
        hits = math.ceil(hits)
        if values['characterinput'] == "Wes":
            weapons *= 0.75
        result0 = damage
        window['output0'].update('You will deal {0} damage.'.format(result0))
        result1 = hits
        window['output1'].update('You will need to hit the enemy {0} times.'.format(result1))
        result2 = 1
        if durability > 0:
            result2 = math.ceil(weapons)
            window['output2'].update('You will need {0} of your weapons.'.format(result2))
        if values['weaponinput'] != "Boomerang" and values['weaponinput'][0:8] != "Alarming" and values['weaponinput'][0:6] != "Trusty":
            result3 = (hits / 2) * 1.05
        if values['weaponinput'][0:8] == "Alarming":
            result3 = (hits / 2) * 1.307 * 1.05
        if values['weaponinput'][0:6] == "Trusty":
            result3 = (hits) * 1.05
        result3 = math.ceil(result3)
        window['output3'].update("You will need around {0} seconds to kill the enemy if you will tank.".format(result3))
        window['Copy to clipboard'].update(disabled=False)
    if event == "Copy to clipboard":
        copy_to_cb("Damage: {}, Hits: {}, Weapons: {}, Seconds: {}".format(result0, result1, result2, result3))

# Finish up by removing from the screen
window.close()
