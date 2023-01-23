import streamlit as st

# reading todo_list from text file
with open("todos.txt", 'r') as file:
    todo_list = file.readlines()

st.title("My Todo App")
st.subheader("This is my first web app")
st.write("This app is to increase your productivity.")

for todo in todo_list:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")
