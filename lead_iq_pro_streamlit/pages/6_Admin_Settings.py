import streamlit as st

st.set_page_config(page_title="Admin Settings", layout="wide")

if not st.session_state.get("authenticated"):
    st.warning("Please log in from the main page.")
    st.stop()

if st.session_state.get("role") != "Admin":
    st.error("Admin access required.")
    st.stop()

st.title("Admin Settings")

st.markdown("### Current User")
st.write(f"Username: **{st.session_state.get('username')}**")
st.write(f"Role: **{st.session_state.get('role')}**")

st.markdown("### Enterprise Roadmap")
st.checkbox("Enable role-based access control", value=True)
st.checkbox("Enable audit logging", value=False)
st.checkbox("Enable database persistence", value=False)
st.checkbox("Enable AI provider integration", value=False)

st.markdown("### Deployment Notes")
st.code("""
# Streamlit Cloud
# Store secrets in .streamlit/secrets.toml

[database]
host = "your-host"
user = "your-user"
password = "your-password"
database = "your-db"

[auth]
admin_password = "replace-this"
""")
