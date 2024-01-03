from modules.file_operations import *


def handle_add_operation(user_action, todo_list):
    todo = user_action[4:] + "\n" if len(user_action) > len("add") else input("Enter a new todo: ").strip() + "\n"
    todo_list.append(todo)


def handle_display_operation(todo_list):
    for index, item in enumerate(todo_list):
        item = item.strip('\n')
        print(f"{index + 1}) {item}")


def handle_edit_operation(user_action, todo_list):
    try:
        index = int(user_action[5:]) if len(user_action) > len("edit") \
            else int(input("Enter a todo index: ").strip())
        index -= 1
        if index >= len(todo_list):
            raise IndexError
        todo_list[index] = input("Enter a new todo: ").strip() + "\n"
    except ValueError:
        print("Your command is not valid.")
    except IndexError:
        print("There is no item with the specified index.")


def handle_complete_operation(user_action, todo_list):
    try:
        index = int(user_action[9:]) if len(user_action) > len("complete") \
            else int(input("Enter a todo index: ").strip())
        index -= 1
        todo_to_remove = todo_list[index].strip('\n')
        todo_list.pop(index)

        print(f"Todo '{todo_to_remove}' was removed from the list.")
    except ValueError:
        print("Your command is not valid.")
    except IndexError:
        print("There is no item with the specified index.")


def run():
    todo_filename = 'todos.txt'
    todo_list = read_todos(filename=todo_filename)

    while True:
        user_action = input("Type add, show, edit, complete or exit: ").strip()  # strip - to avoid spaces in the input

        if user_action.startswith("add"):
            handle_add_operation(user_action, todo_list)

        elif (user_action.startswith("show")) or (user_action.startswith("display")):
            handle_display_operation(todo_list)

        elif user_action.startswith("edit"):
            handle_edit_operation(user_action, todo_list)

        elif user_action.startswith("complete"):
            handle_complete_operation(user_action, todo_list)

        elif user_action.startswith('exit'):
            break
        else:
            print("Command is not valid.")

    write_todos(filename=todo_filename, todos=todo_list)

    print("The program has completed successfully!")


if __name__ == '__main__':
    run()
