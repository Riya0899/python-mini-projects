import streamlit as st 
st.set_page_config(page_title="calculator",layout="centered")

st.title("simple calculator")

if "previous" not in st.session_state:
    st.session_state.previous=""
if "operator" not in st.session_state:
    st.session_state.operator=""
if "current" not in st.session_state:
    st.session_state.current=""

#functions

def press_number(num):
    st.session_state.current += str(num)

def press_clear():
    st.session_state.current=""
    st.session_state.previous=""
    st.session_state.operator=""
    
def press_operator(op):
    if st.session_state.previous == "":
        st.session_state.previous=st.session_state.current
        st.session_state.current=""
    st.session_state.operator=op
        
def calculate():
    current=float(st.session_state.current)   
    previous=float(st.session_state.previous)   
    
    if st.session_state.operator=='+':
        result=previous+current
    elif st.session_state.operator=='-':
        result=previous-current
    elif st.session_state.operator=='*':
        result=previous*current
    elif st.session_state.operator=='/':
        result=previous/current

    st.session_state.previous=str(result)
    st.session_state.current=""
    st.session_state.operator=""

# display

st.text_input("Display",value=st.session_state.previous + " " + st.session_state.operator + " " + st.session_state.current,disabled=True)

# UI 

col1,col2,col3,col4=st.columns(4)

with col1:
    st.button("1",on_click=press_number,args=(1,))
    st.button("2",on_click=press_number,args=(2,))
    st.button("3",on_click=press_number,args=(3,))
    st.button("C",on_click=press_clear)

with col2:
    st.button("4",on_click=press_number,args=(4,))
    st.button("5",on_click=press_number,args=(5,))
    st.button("6",on_click=press_number,args=(6,))
    st.button("=",on_click=calculate)
    
with col3:
    st.button("7",on_click=press_number,args=(7,))
    st.button("8",on_click=press_number,args=(8,))
    st.button("9",on_click=press_number,args=(9,))
    st.button("0",on_click=press_number,args=(0,))

with col4:
    st.button("-",on_click=press_operator,args=("-",))
    st.button("*",on_click=press_operator,args=("*",))
    st.button("/",on_click=press_operator,args=("/",))
    st.button("+",on_click=press_operator,args=("+",))