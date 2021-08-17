import PySimpleGUI as sg
from selector.selector_opencv import run_selector
from template import make_template, is_template_name_valid, get_template_name_list
from ocr.ocr import run_ocr

sg.theme('Dark Blue 3')


def get_window():
    template_name_list = get_template_name_list()
    tab_1 = [[sg.Text("User Choose template, raw image source, cropped image dest, name of output file")],
             [sg.Text("Choose Template", size=(15, 1)),
              sg.Combo(template_name_list, size=(45, 1), key='-TEMPLATE_CHOICE-')],
             [sg.Text("Image Source", size=(15, 1)), sg.InputText(key='-FOLDER1-'), sg.FolderBrowse(target='-FOLDER1-')],
             [sg.Button("Start", size=(10, 1), key="-START_OCR-")]]

    tab_2 = [[sg.Text("Choose Image", size=(15, 1)), sg.InputText(key='-FILE2-'), sg.FileBrowse(target='-FILE2-')],
             [sg.Text("Template Name", size=(15, 1)), sg.InputText(key='-TEMPLATE_NAME-')],
             [sg.Button(button_text="Start", size=(10, 1), key="-start_templates-"),
              sg.Text("", key="-TEMPLATE_TAB_OUTPUT-")]]

    layout = [[sg.TabGroup([[sg.Tab("Perform OCR", tab_1), sg.Tab("Make Templates", tab_2)]])]]

    return sg.Window("Document OCR", layout)


def main():
    window = get_window()
    state = "WAITING"

    while True:
        event, values = window.read()

        # Exit the window
        if event in (sg.WINDOW_CLOSED, '-CANCEL-'):
            break

        # Change state
        if event == "-start_templates-":
            state = "RUN_TEMPLATE"
        elif event == "-START_OCR-":
            state = "RUN_OCR"

        # Run state
        if state == "RUN_TEMPLATE" and values['-FILE2-'] != "":
            if is_template_name_valid(values['-TEMPLATE_NAME-']):
                crop_values = run_selector(values['-FILE2-'])
                make_template(crop_values, values['-TEMPLATE_NAME-'])
                window.Element("-TEMPLATE_TAB_OUTPUT-").Update(value="Template created: {}".format(
                    values['-TEMPLATE_NAME-']))
                window.Element('-TEMPLATE_CHOICE-').Update(values=get_template_name_list())
            state = "WAITING"
        elif state == "RUN_OCR" and values["-FOLDER1-"] != "":
            run_ocr(values["-FOLDER1-"], values["-TEMPLATE_CHOICE-"])
            state = "WAITING"

    window.close()


if __name__ == '__main__':
    main()
