from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
MODEL_DIR = ROOT_DIR / "models"
REPORT_DIR = ROOT_DIR / "reports"

RAW_DATA = DATA_DIR / "Telco-Customer-Churn.csv"
CLEAN_DATA = DATA_DIR / "telco_churn_cleaned.csv"
MODEL_PATH = MODEL_DIR / "churn_pipeline.joblib"

RANDOM_STATE = 42
TEST_SIZE = 0.20
TARGET = "Churn"
ID_COLUMN = "customerID"
