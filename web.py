import streamlit as st

# reading todo_list from text file
with open("todos.txt", 'r') as file:
    todo_list = file.readlines()


def add_todo():
    todo_local = st.session_state['new_todo'] + '\n'
    todo_list.append(todo_local)
    with open("todos.txt", 'w') as file_local:
        file_local.writelines(todo_list)
    st.session_state['new_todo'] = ""


st.title("My Todo App")
st.subheader("This is my first web app")
st.write("This app is to increase your productivity.")

for todo in todo_list:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
