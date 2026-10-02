import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split

from config import CLEAN_DATA, MODEL_PATH, REPORT_DIR, RANDOM_STATE, TEST_SIZE

def main():
    REPORT_DIR.mkdir(exist_ok=True, parents=True)

    df = pd.read_csv(CLEAN_DATA)
    X = df.drop(
        columns=["Churn", "customerID", "tenure_group", "monthly_charge_group"],
        errors="ignore"
    )
    y = df["Churn"].map({"No": 0, "Yes": 1})

    _, X_test, _, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

    model = joblib.load(MODEL_PATH)

    result = permutation_importance(
        model, X_test, y_test,
        scoring="roc_auc",
        n_repeats=5,
        random_state=RANDOM_STATE,
        n_jobs=-1
    )

    importance = pd.Series(
        result.importances_mean,
        index=X_test.columns
    ).sort_values(ascending=False)

    print(importance.head(15))
    importance.to_csv(REPORT_DIR / "permutation_importance.csv")

    importance.head(15).sort_values().plot(kind="barh", figsize=(8, 6))
    plt.title("Permutation Feature Importance")
    plt.xlabel("Mean decrease in ROC-AUC")
    plt.tight_layout()
    plt.savefig(REPORT_DIR / "feature_importance.png", dpi=150)
    plt.close()

if __name__ == "__main__":
    main()
