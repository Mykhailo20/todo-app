import time
# from datetime import date, datetime
"""
# date only
today_date = date.today()

# Textual month, day and year
today_date_str = today_date.strftime("%B %d, %Y")
print("It is " + str(today_date_str))      


# datetime object containing current date and time
now = datetime.now()
dt_str = now.strftime("%B %d, %Y %H:%M:%S")
print("It is " + dt_str + '.')
"""

print("The time is below")
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

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
        # list comprehension
        # todoList = [item.strip('\n') for item in todoList]

        for index, item in enumerate(todoList):
            item = item.strip('\n')
            row = f"{index + 1}) {item}"        # print(str(index+1) + ") " + str(item))
            print(row)
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

            message = f"Todo '{todo_to_remove}' was removed from the list"
            print(message)
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
