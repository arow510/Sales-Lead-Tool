import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")

if not st.session_state.get("authenticated"):
    st.warning("Please log in from the main page.")
    st.stop()

df = st.session_state.get("leads_df")

st.title("Executive Sales Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Leads", len(df))
col2.metric("Hot Leads", int((df["lead_tier"] == "Hot").sum()))
col3.metric("Warm Leads", int((df["lead_tier"] == "Warm").sum()))
col4.metric("Cold Leads", int((df["lead_tier"] == "Cold").sum()))

st.divider()

left, right = st.columns(2)

with left:
    st.markdown("### Leads by Tier")
    tier_counts = df["lead_tier"].value_counts().reset_index()
    tier_counts.columns = ["lead_tier", "count"]
    fig = px.bar(tier_counts, x="lead_tier", y="count")
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown("### Pipeline Value by Stage")
    stage_value = df.groupby("pipeline_stage", as_index=False)["estimated_value"].sum()
    fig = px.bar(stage_value, x="pipeline_stage", y="estimated_value")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("### Lead Source Performance")
source_summary = df.groupby("lead_source", as_index=False).agg(
    total_leads=("lead_id", "count"),
    avg_score=("lead_score", "mean"),
    total_value=("estimated_value", "sum")
)
st.dataframe(source_summary, use_container_width=True)
