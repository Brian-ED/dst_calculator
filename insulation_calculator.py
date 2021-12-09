import PySimpleGUI as sg
hat_dict = { "Winter Hat" : 120, "Beefalo Hat" : 240, "Tam o' Shanter" : 120, "Rabbit Earmuffs" : 60, "Cat Cap" : 60,
             "None" : 0}
dress_dict = { "Dapper Vest" : 60, "Rain Coat" : 60, "Hibernation Vest" : 240, "Puffy Vest" : 240, "Breezy Vest" : 60,
               "None" : 0}
beard_dict = { "Wilson (Tier 3 Beard)" : 135, "Webber (Tier 3 Beard)" : 67.5, "Wilson (Tier 2 Beard)" : 45,
               "Webber (Tier 2 Beard)" : 33.75, "Wilson (Tier 1 Beard)" : 15, "Webber (Tier 1 Beard)" : 11.25,
               "Woodie" : 45, "Were-Woodie" : 240, "Willow/Wes" : -30, "Other characters" : 0}
layout = [
    [sg.Text('Choose your hat:')],
    [sg.InputCombo(('Winter Hat', 'Beefalo Hat', "Tam o' Shanter", "Rabbit Earmuffs", 'Cat Cap', 'None'),key='hat_input', default_value="Winter Hat", enable_events=True)],
    [sg.Text('Choose your dress:')],
    [sg.InputCombo(('Dapper Vest', 'Hibernation Vest', 'Puffy Vest', 'Breezy Vest', 'Rain Coat', 'None'),key='dress_input', default_value="None", enable_events=True)],
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
        values['hat_input'] = "None"
        values['dress_input'] = "None"
    if values['beard_input'] != "Were-Woodie":
        window['hat_input'].update(disabled=False)
        window['dress_input'].update(disabled=False)
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'Calculate':
        insulation_total = hat_dict[values["hat_input"]] + dress_dict[values["dress_input"]] + beard_dict[values["beard_input"]] + 30
        window['output0'].update('You will have {0} insulation.'.format(insulation_total))
        window['output1'].update('You will lose {0} degrees per second.'.format(30/insulation_total))
        window['output2'].update('You will start freezing after {0} seconds.'.format(int(values["degrees_input"])/(30/insulation_total)))

# Finish up by removing from the screen
window.close()
