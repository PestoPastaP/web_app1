"""import streamlit as st"""
"""pip install streamlit"""
"""open Terminal, type % streamlit run web.py and press enter"""
"""in Terminal, type % pip freeze > requirements.txt, press enter to generate
a new file in this folder, this is the file which will be uploaded into the 
server where we host this web app, so that server should know all
the python library, the server need to install in order to run the
web app correctly.
This file shows all packages and version for the streamlit to function correctly
"""
"""
We need to upload file, right click the web.py tab and enable version control
choose Git and go to GitHub account, choose New Reporitory, give a name and Create
Copy that link, go back to Python, right click, Manage remote, paste
We should "Commit" first
"""
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your <b>productivity</b>.",
        unsafe_allow_html=True)

for index, todo in enumurate(todos):
    st.checkbox(todo, key=todo)
"""Assign a signle name to each checkbox by its exact content, 
if key="value" it will make all checkboxes have the same key"""
    if checkbox:
        todos.pop(index) """remove if checked"""
        functions.write(todos)
        del st.session_state[todo] """delete from the dictionary after it was checked"""
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

print("Hello")

"""When deploying a Web app, you should have a streamlit app on a
 stand-alone python program, that means you shouldn't have unrelevant files"""