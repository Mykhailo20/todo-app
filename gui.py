import PySimpleGUI as sg

# reading a todo list from file 'todos.txt'
with open('todos.txt', 'r') as file:
    todoList = file.readlines()

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 10))

while True:
    event, values = window.read()                   # show the parent form (window) with all its elements
    print(event)
    print(values)
    match event:
        case 'Add':
           todoList.append(values['todo']+'\n')
        case sg.WIN_CLOSED:
            break                                   # break the while loop

# writing a changed todo-list to file 'todos.txt'
with open('todos.txt', 'w') as file:
    file.writelines(todoList)

window.close()

