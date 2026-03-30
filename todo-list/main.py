import streamlit as st 
from datetime import datetime
import sqlite3

st.set_page_config(layout="wide")

def create_table():
    conn=sqlite3.connect('todo.db') # table and db creation
    c=conn.cursor() # executes the conn command
    c.execute('''create table if not exists todo_info(task_id integer primary key autoincrement,task_name text not null,task_status text,created_at datetime)''')
    conn.commit() # save 
    conn.close()  # close
    
def add_task(task):
    current_time=datetime.now()
    conn=sqlite3.connect('todo.db')
    c=conn.cursor()
    c.execute('insert into todo_info(task_name,task_status,created_at)values(?,?,?)',(task,'incomplete',current_time))
    conn.commit()
    conn.close()

def get_data():
    conn=sqlite3.connect('todo.db')
    c=conn.cursor()
    c.execute('select task_id,task_name,task_status,created_at from todo_info')
    tasks=c.fetchall()
    conn.commit()
    conn.close()
    return tasks
    
def update_status(task_id,task_status):
    conn=sqlite3.connect('todo.db')
    c=conn.cursor()
    c.execute('update todo_info set task_status=? where task_id=?',(task_status,task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn=sqlite3.connect('todo.db')
    c=conn.cursor()
    c.execute('delete from todo_info where task_id=?',(task_id,))
    conn.commit()
    conn.close()

def main():
    st.title("streamlit app of todo list")
    create_table()
    
    new_task = st.text_input("enter new task")
    if st.button('add task'):
        if new_task:
            add_task(new_task)
            st.success(f"new task {new_task} added successfully")
        else:
            st.warning("please enter a task!")
    
    st.header('Tasks List')
    tasks = get_data()

    for task in tasks:
        task_id, task_name, task_status, created_at = task

        checkbox_id = f"complete_checkbox_{task_id}"  
        delete_button_id = f"delete_button_{task_id}"

    
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.write(f'**Task ID:** {task_id} at {created_at}')

        with col2:
            st.write(f'**Task:** {task_name}')

        with col3:
            if st.checkbox(
                'Mark as Complete' if task_status == 'incomplete' else 'Mark as Incomplete',
                key=checkbox_id
            ):
                new_status = 'complete' if task_status == 'incomplete' else 'incomplete'
                update_status(task_id, new_status)
                st.success(f'Task marked as {new_status.lower()}!')
                st.rerun()

        with col4:
            if st.button('X', key=delete_button_id,type="primary"):
                delete_task(task_id)
                st.success('Task deleted!')
                st.rerun()

        st.write('---')

if __name__ == '__main__':
    main()
