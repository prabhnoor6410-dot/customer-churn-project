import sqlite3
import pandas as pd
from config import CLEAN_DATA, DATA_DIR, REPORT_DIR

def main():
    DATA_DIR.mkdir(exist_ok=True, parents=True)
    REPORT_DIR.mkdir(exist_ok=True, parents=True)

    df = pd.read_csv(CLEAN_DATA)
    db_path = DATA_DIR / "churn.db"

    with sqlite3.connect(db_path) as conn:
        df.to_sql("customers", conn, if_exists="replace", index=False)

        queries = {
            "contract_churn": """
                SELECT Contract,
                       COUNT(*) AS total_customers,
                       SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS churned_customers,
                       ROUND(
                           100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
                           / COUNT(*), 2
                       ) AS churn_rate
                FROM customers
                GROUP BY Contract
                ORDER BY churn_rate DESC;
            """,

            "internet_churn": """
                SELECT InternetService,
                       COUNT(*) AS customers,
                       ROUND(
                           100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
                           / COUNT(*), 2
                       ) AS churn_rate
                FROM customers
                GROUP BY InternetService
                ORDER BY churn_rate DESC;
            """,

            "payment_churn": """
                SELECT PaymentMethod,
                       COUNT(*) AS customers,
                       ROUND(
                           100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
                           / COUNT(*), 2
                       ) AS churn_rate
                FROM customers
                GROUP BY PaymentMethod
                ORDER BY churn_rate DESC;
            """,

            "tenure_segments": """
                SELECT
                    CASE
                        WHEN tenure < 12 THEN 'New'
                        WHEN tenure <= 36 THEN 'Established'
                        ELSE 'Long-term'
                    END AS segment,
                    COUNT(*) AS customers,
                    ROUND(
                        100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
                        / COUNT(*), 2
                    ) AS churn_rate
                FROM customers
                GROUP BY segment
                ORDER BY churn_rate DESC;
            """
        }

        for name, query in queries.items():
            result = pd.read_sql_query(query, conn)
            print(f"\n{name}:")
            print(result.to_string(index=False))
            result.to_csv(REPORT_DIR / f"{name}.csv", index=False)

if __name__ == "__main__":
    main()
