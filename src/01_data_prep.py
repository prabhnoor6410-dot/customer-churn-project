import pandas as pd
from pathlib import Path
from config import RAW_DATA, CLEAN_DATA, DATA_DIR

def load_raw_data(path=RAW_DATA):
    return pd.read_csv(path)

def clean_data(df):
    df = df.copy()

    # Convert TotalCharges to numeric; blank strings become NaN.
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Remove exact duplicate rows.
    df = df.drop_duplicates()

    # Customer ID should be unique.
    df = df.drop_duplicates(subset=["customerID"])

    # Rows without the target cannot be used for supervised learning.
    df = df.dropna(subset=["Churn"])

    # For this dataset, missing TotalCharges normally corresponds to very
    # short-tenure customers. We remove these rows for a simple baseline.
    df = df.dropna(subset=["TotalCharges"])

    return df.reset_index(drop=True)

def add_business_features(df):
    df = df.copy()

    df["tenure_group"] = pd.cut(
        df["tenure"],
        bins=[-1, 12, 24, 48, float("inf")],
        labels=["0-12 months", "13-24 months", "25-48 months", "49+ months"]
    )

    df["monthly_charge_group"] = pd.cut(
        df["MonthlyCharges"],
        bins=[-float("inf"), 40, 70, 100, float("inf")],
        labels=["Low", "Medium", "High", "Very High"]
    )

    return df

def prepare():
    DATA_DIR.mkdir(exist_ok=True, parents=True)
    df = load_raw_data()
    df = clean_data(df)
    df = add_business_features(df)
    df.to_csv(CLEAN_DATA, index=False)
    print(f"Saved {len(df):,} rows to {CLEAN_DATA}")
    return df

if __name__ == "__main__":
    prepare()
