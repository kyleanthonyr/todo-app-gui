import time

import PySimpleGUI as sg

import functions

sg.theme('LightBlue')

# LABEL WIDGETS
label = sg.Text("Type in a to-do: ")
clock = sg.Text('', key='clock')

# INPUT WIDGETS
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
input_box = sg.InputText(tooltip="Enter to-do", key="todo")

# BUTTONS
exit_btn = sg.Button('Exit', size=6)
edit_button = sg.Button("Edit", size=6)
add_button = sg.Button(size=2, image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add a todo", key="Add")
complete_btn = sg.Button("Complete", size=10)
clear_btn = sg.Button("Clear", size=6)

# MAIN GUI WINDOW
window = sg.Window("My TO-DO App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_btn],
                           [exit_btn, clear_btn]],
                   font=('Helvetica', 18))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b %d, %Y %M:%H:%S'))
    match event:
        # ADD to-do feature
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'  # gets the inputted to-do from gui
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window['todo'].update(value="")

        # EDIT Feature
        case 'Edit':
            try:
                selected_todo = values['todos'][0]  # gets the to-do user wishes to edit
                new_todo = values['todo']  # gets new to-do from user input

                todos = functions.get_todos()
                index = todos.index(selected_todo)  # gives the index of the existing to-do the user selected
                todos[index] = new_todo  # replaces old to-do with new one based on its index
                functions.write_todos(todos)  # updates the to-do list with new todos
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 16), title="No Items Selected")

        case 'Complete':
            try:
                selected_todo = values['todos'][0]  # gets the to-do user wishes to edit
                todos = functions.get_todos()

                todos.remove(selected_todo)
                functions.write_todos(todos)

                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 16), title="No Items Selected")

        case 'Clear':
            todos = functions.get_todos()
            todos.clear()
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        # REFRESH to-do in InputBox
        case 'todos':
            # when you have a list box event, point to the input box and update with selected to-do from listbox
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            # handles close window button error
            break
        case 'Exit':
            break

window.close()
