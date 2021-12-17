from constants import *

import PySimpleGUI as sg
import pyperclip

window = sg.Window("DST Speed Calculator", layout)


def updateWindow(stateInput, charInput, headInput,
                 chestInput, handInput, saddlesInput):
    """I simplify all the trues and falses into one function"""
    window["stateInput"].update(disabled=bool(stateInput))
    window["charInput"].update(disabled=bool(charInput))
    window["headInput"].update(disabled=bool(headInput))
    window["chestInput"].update(disabled=bool(chestInput))
    window["handInput"].update(disabled=bool(handInput))
    window["saddlesInput"].update(disabled=bool(saddlesInput))


while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    for i in range(0, len(exceptions_list)):
        if values[exceptions_list[i][0]] == exceptions_list[i][1]:
            updateWindow(exceptions_list[i][2], exceptions_list[i][3],
                         exceptions_list[i][4], exceptions_list[i][5],
                         exceptions_list[i][6], exceptions_list[i][7])

    # When the calculate button has been hit
    # It will calculate all the multipliers selected.
    if event == "Calculate":
        state = charStates_dict[values["stateInput"]]
        character = charMult_dict[values["charInput"]]
        head = headItems_dict[values["headInput"]]
        chest = chestItems_dict[values["chestInput"]]
        hand = handItems_dict[values["handInput"]]
        saddles = saddles_dict[values["saddlesInput"]]

        prevState, prevchar, prevhead, prevchest, prevhand, prevsaddle = \
            0, 0, 0, 0, 0, 0

        for i in range(0, len(exceptions_list)):
            if values[exceptions_list[i][0]] == exceptions_list[i][1]:
                prevState = prevState or 0**exceptions_list[i][2]
                prevchar = prevchar or 0**exceptions_list[i][3]
                prevhead = prevhead or 0**exceptions_list[i][4]
                prevchest = prevchest or 0**exceptions_list[i][5]
                prevhand = prevhand or 0**exceptions_list[i][6]
                prevsaddle = prevsaddle or 0**exceptions_list[i][7]

        speed = (state**prevState) * (character**prevchar) *\
            (head**prevhead) * (chest**prevchest) * \
            (hand**prevhand) * (saddles**prevsaddle)

        # Adds on all the extra speedbuffs, like road, storm, etc.
        for i in range(0, len(exoticMults_names)):
            if values[exoticMults_names[i]]:
                if values["stateInput"] == "Default beefalo" or \
                        values["stateInput"] == "Ornery beefalo" or \
                        values["stateInput"] == "Rider beefalo" or \
                        values["stateInput"] == "Pudgy beefalo":
                    if exoticMults_names[i] != "roadCheck" and \
                            exoticMults_names[i] != "stormCheck":
                        speed *= exoticMults_dict[exoticMults_names[i]]
                        print(speed)
                else:
                    speed *= exoticMults_dict[exoticMults_names[i]]

        window["output0"].update("You will get {0} speed.".format(speed))

    if event == "Copy to clipboard":
        pyperclip.copy("{0}".format(speed))

window.close()
