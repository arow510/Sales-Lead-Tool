import streamlit as st
from utils.scoring import add_score_explanations

st.set_page_config(page_title="Lead Scoring", layout="wide")

if not st.session_state.get("authenticated"):
    st.warning("Please log in from the main page.")
    st.stop()

df = st.session_state.get("leads_df")
df = add_score_explanations(df)

st.title("Lead Scoring")

st.markdown("""
This starter app uses a transparent rule-based scoring model.

Future version:
- Train Logistic Regression, Random Forest, or XGBoost on historical converted/not-converted outcomes
- Add SHAP explanations
- Save model artifacts
- Score new leads automatically
""")

hot_leads = df.sort_values("lead_score", ascending=False).head(25)

st.markdown("### Top 25 Priority Leads")
st.dataframe(
    hot_leads[
        [
            "lead_id",
            "first_name",
            "last_name",
            "company",
            "lead_score",
            "lead_tier",
            "estimated_value",
            "score_explanation"
        ]
    ],
    use_container_width=True
)

selected_id = st.selectbox("Select Lead ID for detail view", df["lead_id"])
lead = df[df["lead_id"] == selected_id].iloc[0]

st.markdown("### Lead Detail")
st.write(f"**Name:** {lead['first_name']} {lead['last_name']}")
st.write(f"**Company:** {lead['company']}")
st.write(f"**Score:** {lead['lead_score']}")
st.write(f"**Tier:** {lead['lead_tier']}")
st.write(f"**Reason:** {lead['score_explanation']}")
st.write(f"**Notes:** {lead['notes']}")
