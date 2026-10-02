# Customer Churn Intelligence — Python Project

## Project objective

Build an end-to-end Data Science system that:
- cleans customer data
- performs EDA and statistics
- performs SQL analysis
- engineers features
- trains classification models
- evaluates churn predictions
- explains model behavior
- provides a Streamlit dashboard
- exposes a FastAPI prediction endpoint

## Project structure

```text
customer_churn_python_project/
├── data/
│   └── Telco-Customer-Churn.csv
├── src/
│   ├── config.py
│   ├── data_prep.py
│   ├── eda.py
│   ├── statistics.py
│   ├── sql_analysis.py
│   ├── advanced_sql.py
│   ├── feature_engineering.py
│   ├── train.py
│   ├── random_forest.py
│   ├── xgboost_model.py
│   ├── evaluate.py
│   ├── explainability.py
│   └── predict.py
├── models/
├── reports/
├── dashboard/
│   └── app.py
├── api/
│   └── main.py
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Place the original dataset at:

```text
data/Telco-Customer-Churn.csv
```

## Recommended execution order

```bash
python src/data_prep.py
python src/eda.py
python src/statistics.py
python src/sql_analysis.py
python src/advanced_sql.py
python src/feature_engineering.py
python src/train.py
python src/random_forest.py
python src/xgboost_model.py
python src/evaluate.py
python src/explainability.py
```

Then run the dashboard:

```bash
streamlit run dashboard/app.py
```

Run the API:

```bash
uvicorn api.main:app --reload
```

## Important

Do not treat model feature importance as causal evidence. Model predictions are statistical estimates and should be validated before being used for real customer interventions.
