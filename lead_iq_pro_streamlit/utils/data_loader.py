import pandas as pd
import numpy as np

def load_sample_data():
    np.random.seed(42)

    lead_sources = ["Website", "Referral", "Campaign", "LinkedIn", "Webinar", "Cold Outreach"]
    regions = ["West", "East", "South", "Midwest"]
    stages = ["New", "Contacted", "Qualified", "Proposal Sent", "Negotiation", "Closed Won", "Closed Lost"]
    product_interest = ["Cloud Services", "Networking", "Cybersecurity", "ERP", "Analytics", "AI Automation"]

    n = 150

    df = pd.DataFrame({
        "lead_id": range(1001, 1001 + n),
        "first_name": np.random.choice(["Aaron", "Maria", "James", "Lisa", "David", "Nina", "Chris", "Tanya"], n),
        "last_name": np.random.choice(["Howard", "Smith", "Johnson", "Brown", "Garcia", "Lee", "Patel", "Wilson"], n),
        "company": np.random.choice(["Acme Corp", "Northstar Health", "Delta Systems", "CloudBridge", "Pioneer Networks"], n),
        "email": [f"lead{i}@example.com" for i in range(1, n + 1)],
        "phone": [f"555-010-{str(i).zfill(4)}" for i in range(1, n + 1)],
        "region": np.random.choice(regions, n),
        "lead_source": np.random.choice(lead_sources, n),
        "product_interest": np.random.choice(product_interest, n),
        "pipeline_stage": np.random.choice(stages, n),
        "estimated_value": np.random.randint(5000, 250000, n),
        "engagement_score": np.random.randint(1, 100, n),
        "company_size": np.random.randint(10, 10000, n),
        "days_since_last_contact": np.random.randint(0, 90, n),
        "notes": np.random.choice([
            "Interested in cloud migration and cost savings.",
            "Asked about cybersecurity and compliance requirements.",
            "Needs follow-up next week.",
            "Budget approved but comparing vendors.",
            "Low urgency but long-term potential.",
            "Requested technical architecture overview."
        ], n)
    })

    df = score_leads(df)
    return df

def score_leads(df):
    df = df.copy()

    score = (
        df["engagement_score"] * 0.45
        + np.where(df["estimated_value"] > 100000, 25, 10)
        + np.where(df["days_since_last_contact"] <= 7, 20, 5)
        + np.where(df["company_size"] > 1000, 10, 3)
    )

    df["lead_score"] = np.clip(score, 0, 100).round(1)

    df["lead_tier"] = pd.cut(
        df["lead_score"],
        bins=[-1, 50, 75, 100],
        labels=["Cold", "Warm", "Hot"]
    ).astype(str)

    return df

def load_uploaded_file(uploaded_file):
    if uploaded_file.name.endswith(".csv"):
        return pd.read_csv(uploaded_file)

    if uploaded_file.name.endswith((".xlsx", ".xls")):
        return pd.read_excel(uploaded_file)

    raise ValueError("Unsupported file type. Please upload CSV or Excel.")
