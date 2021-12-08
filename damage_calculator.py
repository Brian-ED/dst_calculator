import PySimpleGUI as sg
import math
layout = [
    [sg.Text('Choose your weapon:')],
    [sg.InputCombo(('Blow Dart', 'Strident Trident (spell attack)', 'Strident Trident (on a boat)', 'Glass Cutter (attacking a shadow)', 'Dark Sword', 'Glass Cutter',
                    'Electric Dart', 'Ham Bat', 'Weremoose', 'Thulecite Club', 'Tentacle Spike', 'Bat Bat',
                    'Battle Spear', 'Werebeaver (attacking treeguards)', 'Spear', 'Morning Star', 'Werebeaver', "Tail o' Three Cats", 'Strident Trident (attack from land)', 'Boomerang', 'Trusty Slingshot (rocks)', 'Trusty Slingshot (golden rounds)',
                    'Trusty Slingshot (marbles)', 'Trusty Slingshot (slowing down rounds)', 'Trusty Slingshot (cursed rounds)', 'Trusty Slingshot (trinket)'),key='damageinput', enable_events=True)],
    [sg.Text('Choose your character:')],
    [sg.InputCombo(('Wolfgang (mighty)', 'Wigfrid', 'Wendy/Wes', 'Other characters'), size=(20, 1), key='characterinput')],
    [sg.Text('Choose damage buffs:')],
    [sg.Checkbox('',key='chiliinput'), sg.Image(data=chilidata,tooltip='Chili Spice'), sg.Checkbox('', key='electricinput'), sg.Image(data=electricdata,tooltip='Volt Goat Chaud Froid'), sg.Checkbox('', key='wetinput'), sg.Image(data=wetdata,tooltip='Target is Wet')],
    #[sg.Text('Введите прочность вашего оружия (впишите 0, если прочность бесконечна):')],
    #[sg.Input(key='durabilityinput')],
    [sg.Text('Choose durability buffs:')],
    [sg.Checkbox('',key='warbleinput'), sg.Image(data=warbledata,tooltip='Weaponized Warble')],
    [sg.Text("Write your enemy's health:")],
    [sg.Input(key='healthinput')],
    [sg.Text(size=(60,1), key='output0')],
    [sg.Text(size=(60,1), key='output1')],
    [sg.Text(size=(60,1), key='output2')],
    [sg.Button('Calculate'), sg.Button('Exit')]]

window = sg.Window('DST Damage Calculator', layout)


while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    #if (values['damageinput']) == 'Glass Cutter':
        #window['cutterinput'].update(visible=True)
        #window['cutterimage'].update(visible=True)
    if event == 'Calculate':
        damage_dict = { "Dark Sword" : 68} # TODO: finish damage dictionary and add durability dictionary
        if (values['damageinput']) == 'Dark Sword':
            (values['damageinput']) = 68
            (values['durabilityinput']) = 100
        if (values['damageinput']) == 'Glass Cutter':
            (values['damageinput']) = 68
            (values['durabilityinput']) = 75
        if (values['damageinput']) == 'Glass Cutter (attacking a shadow)':
            (values['damageinput']) = 68
            (values['durabilityinput']) = 150
        if (values['damageinput']) == 'Thulecite Club':
            (values['damageinput']) = 59.5
            (values['durabilityinput']) = 150
        if (values['damageinput']) == 'Ham Bat':
            (values['damageinput']) = 59.5
            (values['durabilityinput']) = 0
        if (values['damageinput']) == 'Weremoose':
            (values['damageinput']) = 59.5
            (values['durabilityinput']) = 0
            (values['characterinput']) = 'Other characters'
        if (values['damageinput']) == 'Tentacle Spike':
            (values['damageinput']) = 51
            (values['durabilityinput']) = 100
        if (values['damageinput']) == 'Bat Bat':
            (values['damageinput']) = 42.5
            (values['durabilityinput']) = 75
        if (values['damageinput']) == 'Battle Spear':
            (values['damageinput']) = 42.5
            (values['durabilityinput']) = 200
        if (values['damageinput']) == 'Spear':
            (values['damageinput']) = 34
            (values['durabilityinput']) = 150
        if (values['damageinput']) == 'Morning Star':
            (values['damageinput']) = 28.9
            (values['durabilityinput']) = 720
            electric_weapon = True
        if (values['damageinput']) == "Tail o' Three Cats":
            (values['damageinput']) = 27.2
            (values['durabilityinput']) = 175
        if (values['damageinput']) == 'Boomerang':
            (values['damageinput']) = 27.2
            (values['durabilityinput']) = 10
        if (values['damageinput']) == 'Strident Trident (spell attack)':
            (values['damageinput']) = 85
            (values['durabilityinput']) = 25
        if (values['damageinput']) == 'Strident Trident (on a boat)':
            (values['damageinput']) = 68
            (values['durabilityinput']) = 150
        if (values['damageinput']) == 'Wereneaver':
            (values['damageinput']) = 27.2
            (values['characterinput']) = 'Other characters'
        if (values['damageinput']) == 'Werebeaver (attacking treeguards)':
            (values['damageinput']) = 44.2
            (values['durabilityinput']) = 0
            (values['characterinput']) = 'Other characters'
        if (values['damageinput']) == 'Strident Trident (attacking from land)':
            (values['damageinput']) = 27.2
            (values['durabilityinput']) = 150
        if (values['damageinput']) == 'Electric Dart':
            (values['damageinput']) = 60
            (values['durabilityinput']) = 1
            electric_weapon = True
        if (values['damageinput']) == 'Blow Dart':
            (values['damageinput']) = 100
            (values['durabilityinput']) = 1
        if (values['damageinput']) == 'Trusty Slingshot (rocks)':
            (values['damageinput']) = 17
            (values['durabilityinput']) = 1
            (values['characterinput']) = 'Other characters'
        if (values['damageinput']) == 'Trusty Slingshot (golden rounds)':
            (values['damageinput']) = 34
            (values['durabilityinput']) = 1
            (values['characterinput']) = 'Other characters'
        if (values['damageinput']) == 'Trusty Slingshot (marbles)':
            (values['damageinput']) = 51
            (values['durabilityinput']) = 1
            (values['characterinput']) = 'Other characters'
        if (values['damageinput']) == 'Trusty Slingshot (slowing down rounds)':
            (values['damageinput']) = 17
            (values['durabilityinput']) = 1
            (values['characterinput']) = 'Other characters'
        if (values['damageinput']) == 'Trusty Slingshot (cursed rounds)':
            (values['damageinput']) = 51
            (values['durabilityinput']) = 1
            (values['characterinput']) = 'Other characters'
        if (values['damageinput']) == 'Trusty Slingshot (trinket)':
            (values['damageinput']) = 59.5
            (values['durabilityinput']) = 1
            (values['characterinput']) = 'Other characters'
        if (values['characterinput']) == 'Wolfgang (mighty)':
            (values['damageinput']) = int((values['damageinput'])) * 2
        if (values['characterinput']) == 'Wigfrid':
            (values['damageinput']) = int((values['damageinput'])) * 1.25
        if (values['characterinput']) == 'Wendy/Wes':
            (values['damageinput']) = int((values['damageinput'])) * 0.75
        if electric_weapon:
            (values['electricinput']) = True
        if (values['chiliinput']) == True:
            (values['damageinput']) = int((values['damageinput'])) * 1.2
        if (values['electricinput']) == True:
            if (values['wetinput']) == True:
                (values['damageinput']) = int((values['damageinput'])) * 2.5
            if (values['wetinput']) == False:
                (values['damageinput']) = int((values['damageinput'])) * 1.5
        hits = int((values['healthinput'])) / int((values['damageinput']))
        if int((values['durabilityinput'])) > 0:
            if (values['warbleinput']) == True:
                (values['durabilityinput']) = int((values['durabilityinput'])) * 1.25
            (values['healthinput']) = int((values['healthinput'])) / int((values['damageinput']))
            (values['healthinput']) = int((values['healthinput'])) / int((values['durabilityinput']))
            (values['healthinput']) = math.ceil(values['healthinput'])
        if int((values['durabilityinput'])) < 1:
            window['output2'].update('')
        hits = math.ceil(hits)
        window['output0'].update('You will deal {0} damage.'.format(values['damageinput']))
        window['output1'].update('You will need to hit the enemy {0} times.'.format(hits))
        if int((values['durabilityinput'])) > 0:
            window['output2'].update('You will need {0} of your weapons.'.format(values['healthinput']))

# Finish up by removing from the screen
window.close()
