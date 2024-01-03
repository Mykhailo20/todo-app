import os
import time
import PySimpleGUI as sg

from modules.file_operations import *

todo_filename = 'todos.txt'
if not os.path.exists(todo_filename):
    with open(todo_filename, 'w') as file:
        pass

todo_list = read_todos(filename=todo_filename)

sg.theme("Black")

label_clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=todo_list, key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[label_clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 10))

while True:
    event, values = window.read(timeout=500)     # show the parent form (window) with all its elements
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todo_list.append(values['todo'] + '\n')
            window['todos'].update(values=todo_list)
            window['todo'].update(value="")

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                index = todo_list.index(todo_to_edit)
                todo_list[index] = new_todo

                window['todos'].update(values=todo_list)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 10))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todo_list.remove(todo_to_complete)

                window['todos'].update(values=todo_list)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 10))

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break                                   # break the while loop

write_todos(filename=todo_filename, todos=todo_list)

window.close()
