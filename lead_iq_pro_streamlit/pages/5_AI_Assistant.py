import streamlit as st

st.set_page_config(page_title="AI Assistant", layout="wide")

if not st.session_state.get("authenticated"):
    st.warning("Please log in from the main page.")
    st.stop()

df = st.session_state.get("leads_df")

st.title("AI Sales Assistant")

st.markdown("""
This page is ready for AI integration.

Suggested capabilities:
- Summarize a lead
- Generate a personalized outreach email
- Recommend next best action
- Extract product interest and urgency from notes
- Detect sentiment from customer notes
""")

selected_id = st.selectbox("Select Lead", df["lead_id"])
lead = df[df["lead_id"] == selected_id].iloc[0]

st.markdown("### Selected Lead")
st.write(f"**Name:** {lead['first_name']} {lead['last_name']}")
st.write(f"**Company:** {lead['company']}")
st.write(f"**Product Interest:** {lead['product_interest']}")
st.write(f"**Notes:** {lead['notes']}")

st.divider()

action = st.radio(
    "Choose AI action",
    ["Summarize Lead", "Draft Outreach Email", "Recommend Next Action"]
)

if st.button("Generate"):
    if action == "Summarize Lead":
        st.info(
            f"{lead['first_name']} {lead['last_name']} from {lead['company']} is interested in "
            f"{lead['product_interest']}. Current tier: {lead['lead_tier']} with score {lead['lead_score']}."
        )

    elif action == "Draft Outreach Email":
        st.text_area(
            "Draft Email",
            value=f"""Subject: Following up on your interest in {lead['product_interest']}

Hi {lead['first_name']},

Thank you for your interest in {lead['product_interest']}. Based on our notes, I believe we can help your team evaluate a solution that supports your business goals.

Would you be open to a short follow-up conversation this week?

Best,
Sales Team
""",
            height=250
        )

    elif action == "Recommend Next Action":
        if lead["lead_tier"] == "Hot":
            st.success("Recommended action: Call within 24 hours and prepare a tailored proposal.")
        elif lead["lead_tier"] == "Warm":
            st.warning("Recommended action: Send educational content and schedule follow-up.")
        else:
            st.info("Recommended action: Add to nurture campaign and monitor engagement.")
