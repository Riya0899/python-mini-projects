import streamlit as st
import sqlite3

st.set_page_config(layout="wide")

def get_connection():
    return sqlite3.connect('atm.db')

def create_table():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS account(accno INTEGER PRIMARY KEY AUTOINCREMENT,ac_holder_name TEXT NOT NULL,pin TEXT,balance INTEGER DEFAULT 1000,a_type TEXT)''')
    c.execute("UPDATE account SET balance = 1000 WHERE balance IS NULL")
    conn.commit()
    conn.close()


def get_user(accno):
    if accno is None:
        return None
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM account WHERE accno=?", (int(accno),))
    data = c.fetchone()
    conn.close()
    return data

def get_balance(accno):
    user = get_user(accno)
    if user:
        return user[3] if user[3] is not None else 0
    return None


def deposit(accno, amount):
    user = get_user(accno)
    if not user:
        return "Account not found"
    current_balance = user[3] if user[3] is not None else 0
    new_balance = current_balance + amount
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE account SET balance=? WHERE accno=?", (new_balance, accno))
    conn.commit()
    conn.close()
    return "Deposit Successful"

def withdraw(accno, amount):
    user = get_user(accno)
    if not user:
        return "Account not found"
    current_balance = user[3] if user[3] is not None else 0
    if amount > current_balance:
        return "Insufficient Balance"
    new_balance = current_balance - amount
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE account SET balance=? WHERE accno=?", (new_balance, accno))
    conn.commit()
    conn.close()
    return "Withdraw Successful"

def change_pin(accno, old_pin, new_pin):
    user = get_user(accno)
    if not user:
        return "Account not found"
    if user[2] != old_pin:
        return "Incorrect old PIN"
    if len(new_pin) != 4 or not new_pin.isdigit():
        return "Please enter a valid 4-digit pin"
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE account SET pin=? WHERE accno=?", (new_pin, accno))
    conn.commit()
    conn.close()
    return "PIN Updated Successfully"


if "accno" not in st.session_state:
    st.session_state.accno = None
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"

def signin(accno, pin):
    user = get_user(accno)
    if user and user[2] == pin:
        st.session_state.accno = user[0]
        st.session_state.logged_in = True
        st.session_state.page = "home"
        st.rerun()
    else:
        st.error("Invalid Account Number or PIN")

def login_page():
    st.title("ATM Login")
    accno = st.number_input("Account Number", step=1)
    pin = st.text_input("PIN", type="password")
    if st.button("Login"):
        signin(accno, pin)
    if st.button("Create Account"):
        st.session_state.page = "signup"
        st.rerun()


def signup_page():
    st.title("Create Account")
    name = st.text_input("Name")
    pin = st.text_input("Create PIN", type="password")
    confirm_pin = st.text_input("Confirm PIN", type="password")
    acc_type = st.selectbox("Account Type", ["Saving", "Current"])
    if st.button("Create Account"):
        if name == "":
            st.error("Name cannot be empty")
        elif pin != confirm_pin:
            st.error("PIN does not match")
        elif len(pin) != 4 or not pin.isdigit():
            st.error("Please enter a valid 4-digit pin")
        else:
            conn = get_connection()
            c = conn.cursor()
            c.execute("INSERT INTO account(ac_holder_name, pin, balance, a_type) VALUES (?, ?, ?, ?)",(name, pin, 1000, acc_type))
            conn.commit()
            accno = c.lastrowid
            conn.close()
            st.success(f"Account Created! Your Account Number: {accno}")
    if st.button(" Back"):
        st.session_state.page = "login"
        st.rerun()

def home_page():
    user = get_user(st.session_state.accno)
    if not user:
        st.error(" Please login again.")
        st.session_state.clear()
        st.rerun()
    st.title("ATM Dashboard")

    st.info(f" {user[1]}  |   {user[0]}")
    st.write("---")
    if st.button(" Deposit"):
        st.session_state.page = "deposit"
        st.rerun()

    if st.button(" Withdraw"):
        st.session_state.page = "withdraw"
        st.rerun()

    if st.button(" Check Balance"):
        st.session_state.page = "balance"
        st.rerun()

    if st.button(" Change PIN"):
        st.session_state.page = "pin"
        st.rerun()

    if st.button(" Logout"):
        st.session_state.clear()
        st.rerun()


def deposit_page():
    st.title("Deposit Money")
    amount = st.number_input("Enter amount", min_value=1)
    if st.button("Deposit"):
        msg = deposit(st.session_state.accno, amount)
        if msg == "Deposit Successful":
            st.success(msg)
        else:
            st.error(msg)
    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()
        
def withdraw_page():
    st.title("Withdraw Money")
    amount = st.number_input("Enter amount", min_value=1)
    if st.button("Withdraw"):
        msg = withdraw(st.session_state.accno, amount)
        if msg == "Withdraw Successful":
            st.success(msg)
        else:
            st.error(msg)
    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()

def balance_page():
    st.title("Check Balance")
    bal = get_balance(st.session_state.accno)

    if bal is not None:
        st.success(f" Available Balance: ₹{bal}")
    else:
        st.error("Account not found")
    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()

def pin_page():
    st.title("Change PIN")
    old_pin = st.text_input("Old PIN", type="password")
    new_pin = st.text_input("New PIN", type="password")

    if st.button("Update PIN"):
        msg = change_pin(st.session_state.accno, old_pin, new_pin)
        if msg == "PIN Updated Successfully":
            st.success(msg)
        else:
            st.error(msg)
    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()

def main():
    create_table()

    if st.session_state.page == "login":
        login_page()

    elif st.session_state.page == "signup":
        signup_page()

    elif st.session_state.logged_in:

        if st.session_state.page == "home":
            home_page()

        elif st.session_state.page == "deposit":
            deposit_page()

        elif st.session_state.page == "withdraw":
            withdraw_page()

        elif st.session_state.page == "balance":
            balance_page()

        elif st.session_state.page == "pin":
            pin_page()
            
if __name__ == "__main__":
    main()