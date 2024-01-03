def read_todos(filename):
    """
    Reads the contents of a file and returns it as a list.
    Args:
         filename (string): the name/path to the file from which the data will be read.
    Returns:
         list: the contents of the file as a list/empty list if the specified file does not exist.
    """
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def write_todos(filename, todos):
    """
    Writes the contents of the todo_list to the file todo_filename.
    Args:
        filename (string): the name/path to the file to which the data will be written.
        todos (list): a list whose contents will be written to the file todo_filename.
    Returns:
        None
    """
    with open(filename, 'w') as file:
        file.writelines(todos)
