import pandas as pd
from scipy.stats import ttest_ind
from config import CLEAN_DATA, REPORT_DIR

def main():
    REPORT_DIR.mkdir(exist_ok=True, parents=True)
    df = pd.read_csv(CLEAN_DATA)

    print("Descriptive statistics:")
    print(df[["tenure", "MonthlyCharges", "TotalCharges"]].describe())

    churned = df.loc[df["Churn"] == "Yes", "MonthlyCharges"]
    retained = df.loc[df["Churn"] == "No", "MonthlyCharges"]

    t_stat, p_value = ttest_ind(churned, retained, equal_var=False)

    result = pd.DataFrame([{
        "test": "Welch independent t-test",
        "t_statistic": t_stat,
        "p_value": p_value,
        "churned_mean_monthly_charges": churned.mean(),
        "retained_mean_monthly_charges": retained.mean()
    }])

    print("\nWelch t-test:")
    print(result.to_string(index=False))
    result.to_csv(REPORT_DIR / "monthly_charges_ttest.csv", index=False)

if __name__ == "__main__":
    main()
