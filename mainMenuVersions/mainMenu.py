import temperature_calculator
import WX78CalcMenu
import PySimpleGUI as sg
import speedCalcMenu
import damageCalcMenu

# Layout

mainMenuLayout = [

    [sg.Button("Speed calculator")],
    [sg.Button("WX-78 overcharge calculator")],
    [sg.Button("Temperature calculator")],
    [sg.Button("Damage calculator")],


    # Buttons
    [sg.Button("Exit")]
]

mainMenuWindow = sg.Window("Main menu", mainMenuLayout)

while True:
    mainMenuEvent, mainMenuValues = mainMenuWindow.read()
    
    # See if user wants to quit or window was closed
    if mainMenuEvent == sg.WINDOW_CLOSED or mainMenuEvent == 'Exit':
        break

    if mainMenuEvent == "WX-78 overcharge calculator":
        WX78CalcMenu.WX78Calc()

    if mainMenuEvent == "Temperature calculator":
        temperature_calculator.insulation()

    if mainMenuEvent == "Speed calculator":
        speedCalcMenu.speedCalc()

    if mainMenuEvent == "Damage calculator":
        damageCalcMenu.damageCalc()

mainMenuWindow.close()