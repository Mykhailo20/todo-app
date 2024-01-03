import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

# reading a todo-list from file 'todos.txt'
with open('todos.txt', 'r') as file:
    todoList = file.readlines()

sg.theme("Black")

label_clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=todoList, key="todos",
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
           todoList.append(values['todo']+'\n')
           window['todos'].update(values=todoList)
           window['todo'].update(value="")

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                index = todoList.index(todo_to_edit)
                todoList[index] = new_todo

                window['todos'].update(values=todoList)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 10))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todoList.remove(todo_to_complete)

                window['todos'].update(values=todoList)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 10))

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break                                   # break the while loop

# writing a todo-list to file 'todos.txt'
with open('todos.txt', 'w') as file:
    file.writelines(todoList)

window.close()