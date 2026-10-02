import sys
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from config import CLEAN_DATA, MODEL_PATH

st.set_page_config(
    page_title="Customer Churn Intelligence",
    layout="wide"
)

st.title("Customer Churn Intelligence Dashboard")

df = pd.read_csv(CLEAN_DATA)
model = joblib.load(MODEL_PATH)

c1, c2, c3 = st.columns(3)
c1.metric("Customers", f"{len(df):,}")
c2.metric("Churn Rate", f"{df['Churn'].eq('Yes').mean()*100:.1f}%")
c3.metric("Average Monthly Charge", f"${df['MonthlyCharges'].mean():.2f}")

st.subheader("Churn Rate by Contract")
contract = pd.crosstab(
    df["Contract"], df["Churn"], normalize="index"
) * 100
st.bar_chart(contract)

st.subheader("Customer Data")
st.dataframe(df, use_container_width=True)

st.subheader("Predict Churn for a Customer")

categorical_defaults = {
    "gender": "Female",
    "Partner": "No",
    "Dependents": "No",
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check"
}

cols = st.columns(2)
values = {}

for i, (key, default) in enumerate(categorical_defaults.items()):
    values[key] = cols[i % 2].selectbox(
        key,
        sorted(df[key].dropna().astype(str).unique()),
        index=sorted(df[key].dropna().astype(str).unique()).index(default)
        if default in set(df[key].dropna().astype(str))
        else 0
    )

values["SeniorCitizen"] = st.number_input("SeniorCitizen", 0, 1, 0)
values["tenure"] = st.number_input("tenure", 0, 100, 12)
values["MonthlyCharges"] = st.number_input(
    "MonthlyCharges", 0.0, 500.0, float(df["MonthlyCharges"].median())
)
values["TotalCharges"] = st.number_input(
    "TotalCharges", 0.0, 100000.0, float(df["TotalCharges"].median())
)

if st.button("Predict Churn"):
    X = pd.DataFrame([values])
    probability = float(model.predict_proba(X)[0, 1])

    st.metric(
        "Predicted Churn Probability",
        f"{probability:.1%}"
    )

    if probability >= 0.5:
        st.warning("Model classifies this customer as higher churn risk.")
    else:
        st.success("Model classifies this customer as lower churn risk.")
