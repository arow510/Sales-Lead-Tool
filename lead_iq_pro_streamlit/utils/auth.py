import streamlit as st

USERS = {
    "admin": {
        "password": "admin123",
        "role": "Admin"
    },
    "manager": {
        "password": "manager123",
        "role": "Sales Manager"
    },
    "rep": {
        "password": "rep123",
        "role": "Sales Rep"
    }
}

def login_form():
    st.title("LeadIQ Pro Login")
    st.caption("Demo login. Replace with secure authentication before production.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = USERS.get(username)
        if user and password == user["password"]:
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state.role = user["role"]
            st.rerun()
        else:
            st.error("Invalid username or password.")

def logout_button():
    with st.sidebar:
        st.write(f"Signed in as: **{st.session_state.get('username', 'Unknown')}**")
        st.write(f"Role: **{st.session_state.get('role', 'Unknown')}**")

        if st.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.username = None
            st.session_state.role = None
            st.rerun()
