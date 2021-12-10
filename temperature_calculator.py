import PySimpleGUI as sg
insulation_icon_data = "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"
overheating_icon_data = "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"


def insulation():
    hat_dict = { "Winter Hat" : 120, "Beefalo Hat" : 240, "Tam o' Shanter" : 120, "Rabbit Earmuffs" : 60, "Cat Cap" : 60,
                 "None" : 0}
    dress_dict = { "Dapper Vest" : 60, "Rain Coat" : 60, "Hibernation Vest" : 240, "Puffy Vest" : 240, "Breezy Vest" : 60,
                   "None" : 0}
    hand_dict = { "Bernie" : 30, "None" : 0 }
    beard_dict = { "Wilson (Tier 3 Beard)" : 135, "Webber (Tier 3 Beard)" : 67.5, "Wilson (Tier 2 Beard)" : 45,
                   "Webber (Tier 2 Beard)" : 33.75, "Wilson (Tier 1 Beard)" : 15, "Webber (Tier 1 Beard)" : 11.25,
                   "Woodie" : 45, "Were-Woodie" : 240, "Willow/Wes" : -30, "Other characters" : 0}
    sg.theme("DarkBlue13") # May be changed later
    layout = [
        [sg.Text('Choose your hat:                                                                      '),
         sg.Button("Insulation"), sg.Image(data=insulation_icon_data)],
        [sg.InputCombo(('Winter Hat', 'Beefalo Hat', "Tam o' Shanter", "Rabbit Earmuffs", 'Cat Cap', 'None'),key='hat_input', default_value="Winter Hat", enable_events=True)],
        [sg.Text('Choose your dress:')],
        [sg.InputCombo(('Dapper Vest', 'Hibernation Vest', 'Puffy Vest', 'Breezy Vest', 'Rain Coat', 'None'),key='dress_input', default_value="None", enable_events=True)],
        [sg.Text('Choose item in your hand:')],
        [sg.InputCombo(('Bernie', 'None'),key='hand_input', default_value="None", enable_events=True)],
        [sg.Text('Choose your character:')],
        [sg.InputCombo(('Were-Woodie', 'Wilson (Tier 3 Beard)', 'Webber (Tier 3 Beard)', 'Wilson (Tier 2 Beard)',
                        'Webber (Tier 2 Beard)', 'Woodie', 'Wilson (Tier 1)', "Webber (Tier 1)", "Willow/Wes",
                        'Other characters'), default_value="Other characters", size=(20, 1), key='beard_input',
                       enable_events=True)],
        [sg.Text("Write your temperature:")],
        [sg.Input(key='degrees_input', default_text="50")],
        [sg.Text(size=(60,1), key='output0')],
        [sg.Text(size=(60,1), key='output1')],
        [sg.Text(size=(60,1), key='output2')],
        [sg.Button('Calculate'), sg.Button('Exit')]]

    window = sg.Window('DST Insulation Calculator', layout)

    while True:
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
            insulation_total = hat_dict[values["hat_input"]] + dress_dict[values["dress_input"]] + hand_dict[values['hand_input']] + beard_dict[values["beard_input"]] + 30
            window['output0'].update('You will have {0} insulation.'.format(insulation_total))
            window['output1'].update('You will lose {0} degrees per second.'.format(30/insulation_total))
            window['output2'].update('You will start freezing after {0} seconds/{1} minutes.'.format(int(values["degrees_input"])/(30/insulation_total), (int(values["degrees_input"])/(30/insulation_total))/60))
        if event == 'Insulation':
            break
    window.close()
    overheating_protection()


def overheating_protection():
    hat_dict = {"Eyebrella": 240, "Straw Hat": 60, "Mushroom Funcap": 60, "Pinetree Pioner Hat": 60,
                "Gardener hat": 60, "None": 0}
    dress_dict = {"Chirpy Scarf": 120, "Chirpy Capelet": 240, "Chirpy Cloak": 240, "Floral Shirt": 240,
                  "Summer Frest": 120, "None": 0}
    hand_dict = {"Umbrella": 120, "Pretty Parasol": 120, "None": 0}
    beard_dict = {"Wilson (Tier 3 Beard)": -135, "Webber (Tier 3 Beard)": -67.5, "Wilson (Tier 2 Beard)": -45,
                  "Webber (Tier 2 Beard)": -33.75, "Wilson (Tier 1 Beard)": -15, "Webber (Tier 1 Beard)": -11.25,
                  "Woodie": -45, "Were-Woodie": 240, "Wes": -30, "Willow": 30, "Blooming Wormwood": 60,
                  "Other characters": 0}
    sg.theme("LightBrown11")  # May be changed later
    layout = [
        [sg.Text('Choose your hat:                                                '),
         sg.Button("Overheating Protection"), sg.Image(data=overheating_icon_data)],
        [sg.InputCombo(('Eyebrella', 'Straw Hat', "Mushroom Funcap", 'Pinetree Pioner Hat', 'Gardener Hat', 'None'),
                       key='hat_input', default_value="Eyebrella", enable_events=True)],
        [sg.Text('Choose your dress:')],
        [sg.InputCombo(('Chirpy Scarf', 'Chirpy Capelet', 'Chirpy Cloak', 'Floral Shirt', 'Summer Frest', 'None'),
                       key='dress_input', default_value="None", enable_events=True)],
        [sg.Text('Choose item in your hand:')],
        [sg.InputCombo(('Umbrella', 'Pretty Parasol', 'None'), key='hand_input', default_value="None",
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
        [sg.Button('Calculate'), sg.Button('Exit')]]

    window = sg.Window('DST Insulation Calculator', layout)

    while True:
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
            window['output0'].update('You will have {0} overheating protection.'.format(protection_total))
            window['output1'].update('You will gain {0} degrees per second.'.format(30 / protection_total))
            window['output2'].update('You will start overheating after {0} seconds/{1} minutes.'.format(
                (70 - int(values["degrees_input"])) / (30 / protection_total),
                ((70 - int(values["degrees_input"])) / (30 / protection_total)) / 60))
        if event == 'Overheating Protection':
            break
    window.close()
    insulation()


if __name__ == "__main__":
    insulation()