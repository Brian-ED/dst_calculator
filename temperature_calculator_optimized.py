import PySimpleGUI as sg
import copy
from pyperclip import copy as copy_to_cb


def insulation():
    hat_dict = { "Winter Hat" : 120, "Beefalo Hat" : 240, "Tam o' Shanter" : 120, "Rabbit Earmuffs" : 60, "Cat Cap" : 60,
                 "None" : 0}
    dress_dict = { "Dapper Vest" : 60, "Rain Coat" : 60, "Hibernation Vest" : 240, "Puffy Vest" : 240, "Breezy Vest" : 60,
                   "None" : 0}
    hand_dict = { "Bernie" : 30, "None" : 0 }
    beard_dict = { "Wilson (Tier 3 Beard)" : 135, "Webber (Tier 3 Beard)" : 67.5, "Wilson (Tier 2 Beard)" : 45,
                   "Webber (Tier 2 Beard)" : 33.75, "Wilson (Tier 1 Beard)" : 15, "Webber (Tier 1 Beard)" : 11.25,
                   "Woodie" : 45, "Were-Woodie" : 240, "Willow/Wes" : -30, "Other characters" : 0}
    hat_dict_keys = []
    for i in hat_dict.keys():
        hat_dict_keys.append(i)
    dress_dict_keys = []
    for i in dress_dict.keys():
        dress_dict_keys.append(i)
    hand_dict_keys = []
    for i in hand_dict.keys():
        hand_dict_keys.append(i)
    beard_dict_keys = []
    for i in beard_dict.keys():
        beard_dict_keys.append(i)
    beard_dict_keys2 = copy.copy(beard_dict_keys)
    beard_dict_keys2.append("Overcharged WX-78")
    sg.theme("DarkBlue13") # May be changed later
    layout = [
        [sg.Text('Choose your hat:                                                                                '),
         sg.Button("Insulation", tooltip="Swap to Overheating Protection")],
        [sg.InputCombo((hat_dict_keys),key='hat_input', default_value="Winter Hat", enable_events=True)],
        [sg.Text('Choose your dress:')],
        [sg.InputCombo((dress_dict_keys),key='dress_input', default_value="None", enable_events=True)],
        [sg.Text('Choose item in your hand:')],
        [sg.InputCombo((hand_dict_keys),key='hand_input', default_value="None", enable_events=True)],
        [sg.Text('Choose your character:')],
        [sg.InputCombo((beard_dict_keys2), default_value="Other characters", size=(20, 1),
                       key='beard_input', enable_events=True)],
        [sg.Text("Write your temperature:")],
        [sg.Input(key='degrees_input', default_text="50")],
        [sg.Text(size=(60,1), key='output0')],
        [sg.Text(size=(60,1), key='output1')],
        [sg.Text(size=(60,1), key='output2')],
        [sg.Button('Calculate'), sg.Button('Exit'), sg.Button("Copy to clipboard", disabled=True)]]

    window = sg.Window('DST Insulation Calculator', layout)
    run_i = True
    while run_i:
        event, values = window.read()
        if values['beard_input'] == "Were-Woodie":
            window['hat_input'].update(disabled=True, value="None")
            window['dress_input'].update(disabled=True, value="None")
            window['hand_input'].update(disabled=True, value="None")
            values['hat_input'] = "None"
            values['dress_input'] = "None"
            values['hand_input'] = "None"
        if values['beard_input'] != "Were-Woodie":
            window['hat_input'].update(disabled=False)
            window['dress_input'].update(disabled=False)
            window['hand_input'].update(disabled=False)
        if values['hand_input'] == "Bernie":
            window['beard_input'].update(disabled=True, value="Willow/Wes")
            values['beard_input'] = "Willow/Wes"
        if values['hand_input'] != "Bernie":
            window['beard_input'].update(disabled=False)
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            window.close()
            break
        if event == 'Calculate':
            if values['beard_input'] != "Overcharged WX-78":
                insulation_total = hat_dict[values["hat_input"]] + dress_dict[values["dress_input"]] + hand_dict[values['hand_input']] + beard_dict[values["beard_input"]] + 30
                result0 = insulation_total
                result1 = 30/insulation_total
                result2 = (int(values["degrees_input"])/(30/insulation_total)), ((int(values["degrees_input"])/(30/insulation_total))/60)
                window['output0'].update('You will have {0} insulation.'.format(result0))
                window['output1'].update('You will lose {0} degrees per second.'.format(result1))
                window['output2'].update('You will start freezing after {0} seconds/{1} minutes.'.format(result2[0], result2[1]))
                window['Copy to clipboard'].update(disabled=False)
            else:
                window['output0'].update('You will start freezing only after overcharging will end.')
                window['Copy to clipboard'].update(disabled=True)
        if event == "Copy to clipboard":
            copy_to_cb("Insulation: {0}, Degrees loss per second: {1}, Freezing after: {2} seconds/{3} minutes".format(result0, result1, result2[0], result2[1]))
        if event == 'Insulation':
            run_i = False
            window.close()
            overheating_protection()


def overheating_protection():
    hat_dict = {"Eyebrella": 240, "Straw Hat": 60, "Mushroom Funcap": 60, "Pinetree Pioner Hat": 60,
                "Gardener Hat": 60, "None": 0}
    dress_dict = {"Chirpy Scarf": 120, "Chirpy Capelet": 240, "Chirpy Cloak": 240, "Floral Shirt": 240,
                  "Summer Frest": 120, "None": 0}
    hand_dict = {"Umbrella": 120, "Pretty Parasol": 120, "None": 0}
    beard_dict = {"Wilson (Tier 3 Beard)": -135, "Webber (Tier 3 Beard)": -67.5, "Wilson (Tier 2 Beard)": -45,
                  "Webber (Tier 2 Beard)": -33.75, "Wilson (Tier 1 Beard)": -15, "Webber (Tier 1 Beard)": -11.25,
                  "Woodie": -45, "Were-Woodie": 240, "Wes": -30, "Willow": 30, "Blooming Wormwood": 60,
                  "Other characters": 0}
    hat_dict_keys = []
    for i in hat_dict.keys():
        hat_dict_keys.append(i)
    dress_dict_keys = []
    for i in dress_dict.keys():
        dress_dict_keys.append(i)
    hand_dict_keys = []
    for i in hand_dict.keys():
        hand_dict_keys.append(i)
    beard_dict_keys = []
    for i in beard_dict.keys():
        beard_dict_keys.append(i)
    sg.theme("LightBrown11")  # May be changed later
    layout = [
        [sg.Text('Choose your hat:                                                          '),
         sg.Button("Overheating Protection", tooltip="Swap to Insulation")],
        [sg.InputCombo((hat_dict_keys), key='hat_input', default_value="Eyebrella", enable_events=True)],
        [sg.Text('Choose your dress:')],
        [sg.InputCombo((dress_dict_keys), key='dress_input', default_value="None", enable_events=True)],
        [sg.Text('Choose item in your hand:')],
        [sg.InputCombo((hand_dict_keys), key='hand_input', default_value="None",
                       enable_events=True)],
        [sg.Text('Choose your character:')],
        [sg.InputCombo(('Were-Woodie', 'Wilson (Tier 3 Beard)', 'Webber (Tier 3 Beard)', 'Wilson (Tier 2 Beard)',
                        'Webber (Tier 2 Beard)', 'Woodie', 'Wilson (Tier 1)', "Webber (Tier 1)", "Willow", 'Wes',
                        'Blooming Wormwood', 'Other characters'), default_value="Other characters", size=(20, 1),
                       key='beard_input',
                       enable_events=True)],
        [sg.Text("Write your temperature:")],
        [sg.Input(key='degrees_input', default_text="5")],
        [sg.Text(size=(60, 1), key='output0')],
        [sg.Text(size=(60, 1), key='output1')],
        [sg.Text(size=(60, 1), key='output2')],
        [sg.Button('Calculate'), sg.Button('Exit'), sg.Button("Copy to clipboard", disabled=True)]]

    window = sg.Window('DST Overheating Protection Calculator', layout)
    run_o = True
    while run_o:
        event, values = window.read()
        if values['beard_input'] == "Were-Woodie":
            window['hat_input'].update(disabled=True, value="None")
            window['dress_input'].update(disabled=True, value="None")
            window['hand_input'].update(disabled=True, value="None")
            values['hat_input'] = "None"
            values['dress_input'] = "None"
            values['hand_input'] = "None"
        if values['beard_input'] != "Were-Woodie":
            window['hat_input'].update(disabled=False)
            window['dress_input'].update(disabled=False)
            window['hand_input'].update(disabled=False)
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            window.close()
            break
        if event == 'Calculate':
            protection_total = hat_dict[values["hat_input"]] + dress_dict[values["dress_input"]] + hand_dict[
                values["hand_input"]] + beard_dict[values["beard_input"]] + 30
            result0 = protection_total
            result1 = 30 / protection_total
            result2 = ((70 - int(values["degrees_input"])) / (30 / protection_total)), (((70 - int(values["degrees_input"])) / (30 / protection_total)) / 60)
            window['output0'].update('You will have {0} overheating protection.'.format(protection_total))
            window['output1'].update('You will gain {0} degrees per second.'.format(30 / protection_total))
            window['output2'].update('You will start overheating after {0} seconds/{1} minutes.'.format(
                (70 - int(values["degrees_input"])) / (30 / protection_total),
                ((70 - int(values["degrees_input"])) / (30 / protection_total)) / 60))
            window['Copy to clipboard'].update(disabled=False)
        if event == "Copy to clipboard":
            copy_to_cb("Overheating Protection: {0}, Degrees gain per second: {1}, Overheating after: {2} seconds/{3} minutes".format(result0, result1, result2[0], result2[1]))
        if event == 'Overheating Protection':
            run_o = False
            window.close()
            insulation()


if __name__ == "__main__":
    insulation()