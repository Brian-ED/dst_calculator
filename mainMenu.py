import WX78Calc
# import speedCalc
# import temperature_calculator_optimized as tempCalc
import PySimpleGUI as sg

# Layout

mainMenuLayout = [

    [sg.Button("Speed calculator"), sg.Button("WX-78 overcharge calculator")],
    [sg.Button("Temperature calculator")],


    # Buttons
    [sg.Button("Exit")]
]

mainMenuWindow = sg.Window("Main menu", mainMenuLayout)

while True:
    mainMenuEvent, mainMenuValues = mainMenuWindow.read()
    
    # See if user wants to quit or window was closed
    if mainMenuEvent == sg.WINDOW_CLOSED or mainMenuEvent == 'Exit':
        break
    
#    if event == "Speed calculator":
#        speedCalc()

    if mainMenuEvent == "WX-78 overcharge calculator":
        mainMenuWindow.close()
        WX78Calc.WX78Calcpy()
        break

#    if event == "Temperature calculator":
#        tempCalc()


mainMenuWindow.close()