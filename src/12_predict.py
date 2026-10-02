import joblib
import pandas as pd
from config import MODEL_PATH

def predict_customer(customer_data: dict):
    model = joblib.load(MODEL_PATH)
    X = pd.DataFrame([customer_data])

    probability = float(model.predict_proba(X)[0, 1])
    prediction = int(probability >= 0.5)

    return {
        "churn_probability": probability,
        "prediction": prediction,
        "label": "High risk" if prediction else "Low risk"
    }

if __name__ == "__main__":
    example = {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 5,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 85.0,
        "TotalCharges": 425.0
    }
    print(predict_customer(example))
