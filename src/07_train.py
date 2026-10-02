import json
import joblib
import numpy as np
import pandas as pd

from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, average_precision_score
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from config import CLEAN_DATA, MODEL_DIR, REPORT_DIR, RANDOM_STATE, TEST_SIZE

def build_pipeline(X):
    numeric = X.select_dtypes(include=np.number).columns.tolist()
    categorical = X.select_dtypes(exclude=np.number).columns.tolist()

    preprocessing = ColumnTransformer([
        ("num", Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]), numeric),
        ("cat", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ]), categorical)
    ])

    return Pipeline([
        ("preprocessing", preprocessing),
        ("model", LogisticRegression(
            max_iter=2000,
            class_weight="balanced",
            random_state=RANDOM_STATE
        ))
    ])

def main():
    MODEL_DIR.mkdir(exist_ok=True, parents=True)
    REPORT_DIR.mkdir(exist_ok=True, parents=True)

    df = pd.read_csv(CLEAN_DATA)

    # Keep model features consistent with API/dashboard inputs.
    drop_cols = ["Churn", "customerID", "tenure_group", "monthly_charge_group"]
    X = df.drop(columns=drop_cols, errors="ignore")
    y = df["Churn"].map({"No": 0, "Yes": 1})

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )

    pipeline = build_pipeline(X)
    pipeline.fit(X_train, y_train)

    probability = pipeline.predict_proba(X_test)[:, 1]
    prediction = (probability >= 0.5).astype(int)

    metrics = {
        "accuracy": accuracy_score(y_test, prediction),
        "precision": precision_score(y_test, prediction, zero_division=0),
        "recall": recall_score(y_test, prediction, zero_division=0),
        "f1": f1_score(y_test, prediction, zero_division=0),
        "roc_auc": roc_auc_score(y_test, probability),
        "pr_auc": average_precision_score(y_test, probability)
    }

    joblib.dump(pipeline, MODEL_DIR / "churn_pipeline.joblib")

    with open(REPORT_DIR / "model_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print("\nModel metrics:")
    for k, v in metrics.items():
        print(f"{k:10}: {v:.4f}")

    print(f"\nSaved model: {MODEL_DIR / 'churn_pipeline.joblib'}")

if __name__ == "__main__":
    main()
