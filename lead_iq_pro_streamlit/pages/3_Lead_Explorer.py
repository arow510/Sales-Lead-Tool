import streamlit as st

st.set_page_config(page_title="Lead Explorer", layout="wide")

if not st.session_state.get("authenticated"):
    st.warning("Please log in from the main page.")
    st.stop()

df = st.session_state.get("leads_df")

st.title("Lead Explorer")

with st.sidebar:
    st.header("Filters")

    tier_filter = st.multiselect(
        "Lead Tier",
        options=sorted(df["lead_tier"].unique()),
        default=sorted(df["lead_tier"].unique())
    )

    region_filter = st.multiselect(
        "Region",
        options=sorted(df["region"].unique()),
        default=sorted(df["region"].unique())
    )

    source_filter = st.multiselect(
        "Lead Source",
        options=sorted(df["lead_source"].unique()),
        default=sorted(df["lead_source"].unique())
    )

    min_score = st.slider("Minimum Lead Score", 0, 100, 0)

search = st.text_input("Search name, company, email, product, or notes")

filtered = df[
    (df["lead_tier"].isin(tier_filter))
    & (df["region"].isin(region_filter))
    & (df["lead_source"].isin(source_filter))
    & (df["lead_score"] >= min_score)
]

if search:
    search_lower = search.lower()
    text_cols = ["first_name", "last_name", "company", "email", "product_interest", "notes"]
    mask = filtered[text_cols].astype(str).apply(
        lambda col: col.str.lower().str.contains(search_lower, na=False)
    ).any(axis=1)
    filtered = filtered[mask]

st.write(f"Showing **{len(filtered)}** leads")

st.dataframe(filtered, use_container_width=True)

csv = filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download Filtered Leads",
    data=csv,
    file_name="filtered_leads.csv",
    mime="text/csv"
)
