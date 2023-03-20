import PySimpleGUI as sg

import functions

# 'Add To-do' GUI components
label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")

# MAIN GUI WINDOW
window = sg.Window("My TO-DO App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()

    match event:
        # Add to-do feature
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'  # gets the inputted to-do from gui
            todos.append(new_todo)
            functions.write_todos(todos)

        # handles close window button
        case sg.WIN_CLOSED:
            break

window.close()
