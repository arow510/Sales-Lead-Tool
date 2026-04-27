import pandas as pd
import numpy as np

def explain_score(row):
    reasons = []

    if row.get("engagement_score", 0) >= 75:
        reasons.append("High engagement activity")
    elif row.get("engagement_score", 0) >= 50:
        reasons.append("Moderate engagement activity")
    else:
        reasons.append("Low engagement activity")

    if row.get("estimated_value", 0) >= 100000:
        reasons.append("High estimated opportunity value")

    if row.get("days_since_last_contact", 999) <= 7:
        reasons.append("Recently contacted or recently active")
    elif row.get("days_since_last_contact", 999) > 30:
        reasons.append("Needs follow-up due to inactivity")

    if row.get("company_size", 0) >= 1000:
        reasons.append("Large company size")

    return "; ".join(reasons)

def add_score_explanations(df):
    df = df.copy()
    df["score_explanation"] = df.apply(explain_score, axis=1)
    return df
