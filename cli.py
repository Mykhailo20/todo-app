import time

print(f"Current time: {time.strftime('%b %d, %Y %H:%M:%S')}")

user_prompt = "Enter a todo: "
with open('todos.txt', 'r') as file:
    todoList = file.readlines()

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()  # to avoid spaces in the input

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todoList.append(todo)

    elif (user_action.startswith('show')) or (user_action.startswith('display')):
        for index, item in enumerate(todoList):
            item = item.strip('\n')
            print(f"{index + 1}) {item}")
    elif user_action.startswith("edit"):
        try:
            index = int(user_action[5:])
            index -= 1
            todoList[index] = input("Enter a new todo: ").strip() + "\n"
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
            todo_to_remove = todoList[index].strip('\n')
            todoList.pop(index)

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

with open('todos.txt', 'w') as file:
    file.writelines(todoList)

print("The program has completed successfully!")