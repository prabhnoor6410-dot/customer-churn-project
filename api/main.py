from pathlib import Path
import sys

import joblib
import pandas as pd

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


# --------------------------------------------------
# PROJECT PATH
# --------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(ROOT / "src"))

from config import MODEL_PATH


# --------------------------------------------------
# FASTAPI APP
# --------------------------------------------------

app = FastAPI(
    title="Customer Churn Intelligence API",
    description="Machine Learning API for Customer Churn Prediction",
    version="1.0.0",
)


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://customer-churn-project-eight.vercel.app",
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# CUSTOMER INPUT MODEL
# --------------------------------------------------

class Customer(BaseModel):

    gender: str

    SeniorCitizen: int

    Partner: str

    Dependents: str

    tenure: int

    PhoneService: str

    MultipleLines: str

    InternetService: str

    OnlineSecurity: str

    OnlineBackup: str

    DeviceProtection: str

    TechSupport: str

    StreamingTV: str

    StreamingMovies: str

    Contract: str

    PaperlessBilling: str

    PaymentMethod: str

    MonthlyCharges: float

    TotalCharges: float


# --------------------------------------------------
# HOME ROUTE
# --------------------------------------------------

@app.get("/")
def root():

    return {
        "message": "Customer Churn API is running",
        "status": "online"
    }


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "model_loaded": True
    }


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

@app.post("/predict")
def predict(customer: Customer):

    data = pd.DataFrame(
        [customer.model_dump()]
    )

    probability = float(
        model.predict_proba(data)[0][1]
    )

    prediction = (
        "Yes"
        if probability >= 0.5
        else "No"
    )

    return {
        "churn_prediction": prediction,
        "churn_probability": probability
    }