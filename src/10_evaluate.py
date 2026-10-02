import json
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_curve,
    precision_recall_curve,
    roc_auc_score,
    average_precision_score
)
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
    probability = model.predict_proba(X_test)[:, 1]
    prediction = (probability >= 0.5).astype(int)

    print(classification_report(y_test, prediction))

    cm = confusion_matrix(y_test, prediction)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.savefig(REPORT_DIR / "confusion_matrix.png", dpi=150)
    plt.close()

    fpr, tpr, _ = roc_curve(y_test, probability)
    plt.plot(fpr, tpr, label=f"AUC = {roc_auc_score(y_test, probability):.3f}")
    plt.plot([0, 1], [0, 1], "--")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.tight_layout()
    plt.savefig(REPORT_DIR / "roc_curve.png", dpi=150)
    plt.close()

    precision, recall, _ = precision_recall_curve(y_test, probability)
    plt.plot(recall, precision)
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Precision-Recall Curve")
    plt.tight_layout()
    plt.savefig(REPORT_DIR / "precision_recall_curve.png", dpi=150)
    plt.close()

    print("ROC-AUC:", roc_auc_score(y_test, probability))
    print("PR-AUC:", average_precision_score(y_test, probability))

if __name__ == "__main__":
    main()
