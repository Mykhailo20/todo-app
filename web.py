import streamlit as st

from modules.file_operations import *


def add_todo(filename):
    """
    Adds a new task to the todo list
    Args:
         filename (string): the name/path to the file to which the data will be written.
    Returns:
        None
    """
    todo_local = st.session_state['new_todo'] + '\n'
    todo_list.append(todo_local)
    write_todos(filename=filename, todos=todo_list)
    st.session_state['new_todo'] = ""


st.title("My Todo App")
st.subheader("This is my first web app")
st.write("This app is to increase your productivity.")

todo_filename = 'todos.txt'
todo_list = read_todos(filename=todo_filename)

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(index)
        write_todos(filename=todo_filename, todos=todo_list)
        del st.session_state[todo]
        st.experimental_rerun()
        
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
