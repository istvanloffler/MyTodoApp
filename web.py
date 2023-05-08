import streamlit as st
import functions

todos = functions.get_todos()
checkboxes = []

def add_todo():
    if st.session_state["new_todo"] != "":
        todo = st.session_state["new_todo"] + '\n'
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state.new_todo = ""


def complete_todo():
    for index, checkbox in enumerate(checkboxes):
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[todo]
            checkboxes.pop(checkbox)


st.title("Todo App")
st.subheader("This is my todo app")
st.write("to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    checkboxes.append(checkbox)
    #if checkbox:
        #todos.pop(index)
        #functions.write_todos(todos)
        #del st.session_state[todo]
        #st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='new_todo')

st.button(label="Complete", key="Complete", on_click=complete_todo())

st.session_state
