import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import CLEAN_DATA, REPORT_DIR

def churn_rate_table(df, column):
    table = pd.crosstab(df[column], df["Churn"], normalize="index") * 100
    return table.round(2)

def main():
    REPORT_DIR.mkdir(exist_ok=True, parents=True)
    df = pd.read_csv(CLEAN_DATA)

    print("\nShape:", df.shape)
    print("\nChurn distribution:")
    print(df["Churn"].value_counts())
    print("\nChurn rate:")
    print(df["Churn"].value_counts(normalize=True).mul(100).round(2))

    for col in ["Contract", "InternetService", "PaymentMethod"]:
        table = churn_rate_table(df, col)
        print(f"\n{col} churn rate:")
        print(table)
        table.to_csv(REPORT_DIR / f"{col.lower()}_churn_rate.csv")

    sns.set_theme()
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x="Churn", ax=ax)
    ax.set_title("Customer Churn Distribution")
    fig.tight_layout()
    fig.savefig(REPORT_DIR / "churn_distribution.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 5))
    contract = pd.crosstab(df["Contract"], df["Churn"], normalize="index") * 100
    contract.plot(kind="bar", ax=ax)
    ax.set_ylabel("Percentage")
    ax.set_title("Churn Rate by Contract")
    ax.tick_params(axis="x", rotation=0)
    fig.tight_layout()
    fig.savefig(REPORT_DIR / "contract_churn.png", dpi=150)
    plt.close(fig)

if __name__ == "__main__":
    main()
