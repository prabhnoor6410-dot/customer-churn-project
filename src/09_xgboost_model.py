import joblib
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from config import CLEAN_DATA, MODEL_DIR, RANDOM_STATE, TEST_SIZE

def main():
    try:
        from xgboost import XGBClassifier
    except ImportError:
        raise SystemExit("Install XGBoost first: pip install xgboost")

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
        ("model", XGBClassifier(
            n_estimators=300,
            max_depth=4,
            learning_rate=0.05,
            subsample=0.8,
            colsample_bytree=0.8,
            eval_metric="logloss",
            random_state=RANDOM_STATE
        ))
    ])

    model.fit(X_train, y_train)
    probability = model.predict_proba(X_test)[:, 1]

    print("XGBoost ROC-AUC:", roc_auc_score(y_test, probability))

    MODEL_DIR.mkdir(exist_ok=True, parents=True)
    joblib.dump(model, MODEL_DIR / "xgboost_pipeline.joblib")

if __name__ == "__main__":
    main()
