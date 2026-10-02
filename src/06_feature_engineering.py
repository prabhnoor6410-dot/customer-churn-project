import pandas as pd
import numpy as np
from config import CLEAN_DATA, DATA_DIR

def engineer_features(df):
    df = df.copy()

    df["avg_monthly_charge_per_tenure"] = (
        df["TotalCharges"] / df["tenure"].replace(0, np.nan)
    ).fillna(df["MonthlyCharges"])

    df["has_security_service"] = (
        (df["OnlineSecurity"] == "Yes") |
        (df["OnlineBackup"] == "Yes") |
        (df["DeviceProtection"] == "Yes") |
        (df["TechSupport"] == "Yes")
    ).astype(int)

    df["streaming_user"] = (
        (df["StreamingTV"] == "Yes") |
        (df["StreamingMovies"] == "Yes")
    ).astype(int)

    return df

def main():
    df = pd.read_csv(CLEAN_DATA)
    df = engineer_features(df)

    output = DATA_DIR / "telco_churn_features.csv"
    df.to_csv(output, index=False)
    print(f"Saved engineered dataset to {output}")

if __name__ == "__main__":
    main()
