import streamlit as st
from utils.auth import login_form, logout_button
from utils.data_loader import load_sample_data

st.set_page_config(
    page_title="LeadIQ Pro",
    page_icon="📊",
    layout="wide"
)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    login_form()
    st.stop()

logout_button()

st.title("LeadIQ Pro")
st.subheader("AI-Powered Sales Lead Intelligence Platform")

st.markdown("""
Welcome to **LeadIQ Pro**, an enterprise-style Streamlit application for sales lead management, scoring, and analytics.

Use the left sidebar to navigate:
- Dashboard
- Upload Leads
- Lead Explorer
- Lead Scoring
- AI Assistant
- Admin Settings
""")

if "leads_df" not in st.session_state:
    st.session_state.leads_df = load_sample_data()

df = st.session_state.leads_df

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Leads", len(df))

with col2:
    st.metric("Hot Leads", int((df["lead_tier"] == "Hot").sum()))

with col3:
    avg_score = round(df["lead_score"].mean(), 1)
    st.metric("Average Score", avg_score)

with col4:
    pipeline_value = df["estimated_value"].sum()
    st.metric("Pipeline Value", f"${pipeline_value:,.0f}")

st.divider()

st.markdown("### Recent Lead Sample")
st.dataframe(df.head(10), use_container_width=True)
