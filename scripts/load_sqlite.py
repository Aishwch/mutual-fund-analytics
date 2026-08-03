import os
import pandas as pd
from sqlalchemy import create_engine

# ==========================================================
# CREATE SQLITE CONNECTION
# ==========================================================

db_path = "sql/bluestock_mf.db"
engine = create_engine(f"sqlite:///{db_path}")

print("=" * 60)
print("LOADING CLEANED DATA INTO SQLITE")
print("=" * 60)

# ==========================================================
# LIST OF CLEANED FILES
# ==========================================================

files = [
    "01_fund_master_cleaned.csv",
    "02_nav_history_cleaned.csv",
    "03_aum_by_fund_house_cleaned.csv",
    "04_monthly_sip_inflows_cleaned.csv",
    "05_category_inflows_cleaned.csv",
    "06_industry_folio_count_cleaned.csv",
    "07_scheme_performance_cleaned.csv",
    "08_investor_transactions_cleaned.csv",
    "09_portfolio_holdings_cleaned.csv",
    "10_benchmark_indices_cleaned.csv"
]

# ==========================================================
# LOAD EACH CSV
# ==========================================================

for file in files:

    path = os.path.join("data", "processed", file)

    if not os.path.exists(path):
        print(f"❌ File not found: {file}")
        continue

    df = pd.read_csv(path)

    table_name = file.replace("_cleaned.csv", "")

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"✓ {table_name:<35} Rows Loaded: {len(df)}")

print("=" * 60)
print("ALL CLEANED DATA LOADED SUCCESSFULLY")
print("=" * 60)