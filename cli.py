import time

from modules.file_operations import *

todo_filename = 'todos.txt'
todo_list = read_todos(filename=todo_filename)

print(f"Current time: {time.strftime('%b %d, %Y %H:%M:%S')}")
user_prompt = "Enter a todo: "

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()  # to avoid spaces in the input

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todo_list.append(todo)

    elif (user_action.startswith('show')) or (user_action.startswith('display')):
        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            print(f"{index + 1}) {item}")
    elif user_action.startswith("edit"):
        try:
            index = int(user_action[5:])
            index -= 1
            todo_list[index] = input("Enter a new todo: ").strip() + "\n"
        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("There is no item with that index.")
            continue

    elif user_action.startswith('complete'):
        try:
            index = int(user_action[9:])
            index -= 1
            todo_to_remove = todo_list[index].strip('\n')
            todo_list.pop(index)

            print(f"Todo '{todo_to_remove}' was removed from the list")
        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("There is no item with that index.")
            continue
            
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid.")

write_todos(filename=todo_filename, todos=todo_list)

print("The program has completed successfully!")
