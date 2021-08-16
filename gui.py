import PySimpleGUI as sg
from selector.selector_opencv import run_selector

sg.theme('Dark Blue 3')


def run_gui():
    form_rows = [[sg.Text("Perform OCR", font='Any 14')],
                 [sg.Text("User Choose template, raw image source, cropped image dest, name of output file")],
                 [sg.Submit(size=(10, 1)), sg.Cancel(size=(10, 1))],
                 [sg.Text("Make Templates", font='Any 14')],
                 [sg.Text("Choose Image", size=(15, 1)), sg.InputText(key='-file2-'), sg.FileBrowse(target='-file2-')],
                 [sg.Button(button_text="Start", size=(10, 1), key="-start_templates-"), sg.Cancel(size=(10, 1))]]

    window = sg.Window("Document OCR", form_rows)
    event, values = window.read()
    window.close()
    return event, values


def main():
    button, values = run_gui()
    state = "WAITING"

    while True:
        # f1, f2 = values['-file1-'], values['-file2-']
        if button == "-start_templates-":
            state = "RUN_TEMPLATE"

        if state == "RUN_TEMPLATE" and values['-file2-'] != "":
            run_selector(values['-file2-'])
            state = "WAITING"
        elif state == "RUN_OCR":
            print("TO DO: RUN OCR")


if __name__ == '__main__':
    main()
