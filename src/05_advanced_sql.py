import sqlite3
import numpy as np
import pandas as pd
from config import CLEAN_DATA, DATA_DIR, REPORT_DIR

def main():
    REPORT_DIR.mkdir(exist_ok=True, parents=True)
    df = pd.read_csv(CLEAN_DATA)

    rng = np.random.default_rng(42)
    support_tickets = pd.DataFrame({
        "customerID": df["customerID"],
        "ticket_count": rng.poisson(1.2, len(df))
    })

    with sqlite3.connect(DATA_DIR / "churn.db") as conn:
        df.to_sql("customers", conn, if_exists="replace", index=False)
        support_tickets.to_sql("support_tickets", conn, if_exists="replace", index=False)

        queries = {
            "join_analysis": """
                SELECT c.Contract,
                       COUNT(*) AS customers,
                       ROUND(AVG(s.ticket_count), 2) AS avg_tickets
                FROM customers c
                LEFT JOIN support_tickets s
                ON c.customerID = s.customerID
                GROUP BY c.Contract;
            """,
            "high_charge_customers": """
                SELECT customerID, MonthlyCharges
                FROM customers
                WHERE MonthlyCharges > (
                    SELECT AVG(MonthlyCharges) FROM customers
                )
                ORDER BY MonthlyCharges DESC
                LIMIT 20;
            """,
            "cte_contract": """
                WITH stats AS (
                    SELECT Contract,
                           COUNT(*) AS total_customers,
                           SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS churned
                    FROM customers
                    GROUP BY Contract
                )
                SELECT Contract, total_customers, churned,
                       ROUND(100.0 * churned / total_customers, 2) AS churn_rate
                FROM stats
                ORDER BY churn_rate DESC;
            """,
            "window_ranking": """
                SELECT customerID, Contract, MonthlyCharges,
                       RANK() OVER (
                           PARTITION BY Contract
                           ORDER BY MonthlyCharges DESC
                       ) AS charge_rank
                FROM customers
                ORDER BY Contract, charge_rank
                LIMIT 100;
            """
        }

        for name, query in queries.items():
            result = pd.read_sql_query(query, conn)
            print(f"\n{name}:")
            print(result.head(20).to_string(index=False))
            result.to_csv(REPORT_DIR / f"{name}.csv", index=False)

if __name__ == "__main__":
    main()
