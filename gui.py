import PySimpleGUI as sg

# reading a todo-list from file 'todos.txt'
with open('todos.txt', 'r') as file:
    todoList = file.readlines()

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=todoList, key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 10))

while True:
    event, values = window.read()                   # show the parent form (window) with all its elements
    print(event)
    print(values)
    match event:
        case 'Add':
           todoList.append(values['todo']+'\n')
           window['todos'].update(values=todoList)

        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            index = todoList.index(todo_to_edit)
            todoList[index] = new_todo

            window['todos'].update(values=todoList)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break                                   # break the while loop

# writing a todo-list to file 'todos.txt'
with open('todos.txt', 'w') as file:
    file.writelines(todoList)

window.close()

