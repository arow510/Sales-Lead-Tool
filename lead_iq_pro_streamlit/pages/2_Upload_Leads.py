import streamlit as st
from utils.data_loader import load_uploaded_file, score_leads

st.set_page_config(page_title="Upload Leads", layout="wide")

if not st.session_state.get("authenticated"):
    st.warning("Please log in from the main page.")
    st.stop()

st.title("Upload Leads")

st.markdown("""
Upload a CSV or Excel file. Recommended columns:

- lead_id
- first_name
- last_name
- company
- email
- phone
- region
- lead_source
- product_interest
- pipeline_stage
- estimated_value
- engagement_score
- company_size
- days_since_last_contact
- notes
""")

uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx", "xls"])

if uploaded_file:
    try:
        df = load_uploaded_file(uploaded_file)

        required_for_scoring = {
            "estimated_value",
            "engagement_score",
            "company_size",
            "days_since_last_contact"
        }

        missing = required_for_scoring - set(df.columns)

        if missing:
            st.warning(f"Missing scoring columns: {missing}. File loaded without scoring.")
        else:
            df = score_leads(df)

        st.session_state.leads_df = df

        st.success("File uploaded successfully.")
        st.dataframe(df.head(20), use_container_width=True)

    except Exception as e:
        st.error(f"Upload failed: {e}")
