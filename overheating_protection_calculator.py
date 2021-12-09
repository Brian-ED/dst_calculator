import PySimpleGUI as sg
hat_dict = { "Eyebrella" : 240, "Straw Hat" : 60, "Mushroom Funcap" : 60, "Pinetree Pioner Hat" : 60,
             "Gardener hat" : 60, "None" : 0 }
dress_dict = { "Chirpy Scarf" : 120, "Chirpy Capelet" : 240, "Chirpy Cloak" : 240, "Floral Shirt" : 240,
               "Summer Frest" : 120, "None" : 0 }
hand_dict = { "Umbrella" : 120, "Pretty Parasol" : 120, "None" : 0 }
beard_dict = { "Wilson (Tier 3 Beard)" : -135, "Webber (Tier 3 Beard)" : -67.5, "Wilson (Tier 2 Beard)" : -45,
               "Webber (Tier 2 Beard)" : -33.75, "Wilson (Tier 1 Beard)" : -15, "Webber (Tier 1 Beard)" : -11.25,
               "Woodie" : -45, "Were-Woodie" : 240, "Wes" : -30, "Willow" : 30, "Blooming Wormwood" : 60, "Other characters" : 0 }
layout = [
    [sg.Text('Choose your hat:')],
    [sg.InputCombo(('Eyebrella', 'Straw Hat', "Mushroom Funcap", 'Pinetree Pioner Hat', 'Gardener Hat', 'None'),key='hat_input', default_value="Eyebrella", enable_events=True)],
    [sg.Text('Choose your dress:')],
    [sg.InputCombo(('Chirpy Scarf', 'Chirpy Capelet', 'Chirpy Cloak', 'Floral Shirt', 'Summer Frest', 'None'),key='dress_input', default_value="None", enable_events=True)],
    [sg.Text('Choose item in your hand:')],
    [sg.InputCombo(('Umbrella', 'Pretty Parasol', 'None'),key='hand_input', default_value="None", enable_events=True)],
    [sg.Text('Choose your character:')],
    [sg.InputCombo(('Were-Woodie', 'Wilson (Tier 3 Beard)', 'Webber (Tier 3 Beard)', 'Wilson (Tier 2 Beard)',
                    'Webber (Tier 2 Beard)', 'Woodie', 'Wilson (Tier 1)', "Webber (Tier 1)", "Willow", 'Wes',
                    'Blooming Wormwood', 'Other characters'), default_value="Other characters", size=(20, 1), key='beard_input',
                   enable_events=True)],
    [sg.Text("Write your temperature:")],
    [sg.Input(key='degrees_input', default_text="5")],
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
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'Calculate':
        protection_total = hat_dict[values["hat_input"]] + dress_dict[values["dress_input"]] + hand_dict[values["hand_input"]] + beard_dict[values["beard_input"]] + 30
        window['output0'].update('You will have {0} overheating protection.'.format(protection_total))
        window['output1'].update('You will gain {0} degrees per second.'.format(30/protection_total))
        window['output2'].update('You will start overheating after {0} seconds.'.format((70-int(values["degrees_input"]))/(30/protection_total)))

# Finish up by removing from the screen
window.close()
