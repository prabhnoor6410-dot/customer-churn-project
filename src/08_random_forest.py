import joblib
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from config import CLEAN_DATA, MODEL_DIR, RANDOM_STATE, TEST_SIZE

def main():
    df = pd.read_csv(CLEAN_DATA)
    X = df.drop(
        columns=["Churn", "customerID", "tenure_group", "monthly_charge_group"],
        errors="ignore"
    )
    y = df["Churn"].map({"No": 0, "Yes": 1})

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

    num = X.select_dtypes(include=np.number).columns
    cat = X.select_dtypes(exclude=np.number).columns

    prep = ColumnTransformer([
        ("num", SimpleImputer(strategy="median"), num),
        ("cat", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ]), cat)
    ])

    model = Pipeline([
        ("preprocessing", prep),
        ("model", RandomForestClassifier(
            n_estimators=400,
            class_weight="balanced",
            random_state=RANDOM_STATE,
            n_jobs=-1
        ))
    ])

    model.fit(X_train, y_train)
    probability = model.predict_proba(X_test)[:, 1]

    print("Random Forest ROC-AUC:", roc_auc_score(y_test, probability))

    MODEL_DIR.mkdir(exist_ok=True, parents=True)
    joblib.dump(model, MODEL_DIR / "random_forest_pipeline.joblib")

if __name__ == "__main__":
    main()
