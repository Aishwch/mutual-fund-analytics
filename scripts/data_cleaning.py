import pandas as pd
import os

# ==========================================================
# CREATE PROCESSED FOLDER
# ==========================================================
os.makedirs("data/processed", exist_ok=True)

print("=" * 60)
print("MUTUAL FUND DATA CLEANING PIPELINE")
print("=" * 60)


# ==========================================================
# HELPER FUNCTION
# ==========================================================
def load_dataset(file_name):
    path = f"data/raw/{file_name}"
    df = pd.read_csv(path)

    print(f"\nLoading: {file_name}")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    return df


# ==========================================================
# 01. FUND MASTER
# ==========================================================

fund_master = load_dataset("01_fund_master.csv")

print("\n========== FUND MASTER PREVIEW ==========")
print(fund_master.head())

print("\nData Types:")
print(fund_master.dtypes)

print("\nMissing Values:")
print(fund_master.isnull().sum())

print("\nDuplicate Rows:")
print(fund_master.duplicated().sum())

# Save cleaned dataset
fund_master.to_csv(
    "data/processed/01_fund_master_cleaned.csv",
    index=False
)

print("✓ Cleaned Fund Master saved.")


# ==========================================================
# 02. NAV HISTORY
# ==========================================================

nav_history = load_dataset("02_nav_history.csv")

print("\n========== NAV HISTORY PREVIEW ==========")
print(nav_history.head())

print("\nData Types:")
print(nav_history.dtypes)

print("\nMissing Values:")
print(nav_history.isnull().sum())

print("\nDuplicate Rows:")
print(nav_history.duplicated().sum())

print("\n========== CLEANING NAV HISTORY ==========")

# Convert Date
nav_history["date"] = pd.to_datetime(nav_history["date"])

# Sort data
nav_history = nav_history.sort_values(
    by=["amfi_code", "date"]
)

print("✓ Date converted to datetime")
print("✓ Data sorted successfully")

# Validate NAV
invalid_nav = nav_history[
    nav_history["nav"] <= 0
]

print(f"\nInvalid NAV Records: {len(invalid_nav)}")

if len(invalid_nav) == 0:
    print("✓ All NAV values are valid.")
else:
    print("⚠ Invalid NAV values found!")

# Fill Missing NAV
nav_history["nav"] = (
    nav_history
    .groupby("amfi_code")["nav"]
    .ffill()
)

print("✓ Missing NAV values forward-filled (if any)")

# Save
nav_history.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

print("✓ Cleaned NAV History saved.")


# ==========================================================
# 08. INVESTOR TRANSACTIONS
# ==========================================================

investor_transactions = load_dataset(
    "08_investor_transactions.csv"
)

print("\n========== INVESTOR TRANSACTIONS PREVIEW ==========")
print(investor_transactions.head())

print("\nData Types:")
print(investor_transactions.dtypes)

print("\nMissing Values:")
print(investor_transactions.isnull().sum())

print("\nDuplicate Rows:")
print(investor_transactions.duplicated().sum())

print("\n========== CLEANING INVESTOR TRANSACTIONS ==========")

# Convert Date
investor_transactions["transaction_date"] = pd.to_datetime(
    investor_transactions["transaction_date"]
)

print("✓ Transaction date converted to datetime")

# Standardize Transaction Type
investor_transactions["transaction_type"] = (
    investor_transactions["transaction_type"]
    .str.strip()
    .str.title()
)

print("✓ Transaction types standardized")

# Validate Amount
invalid_amount = investor_transactions[
    investor_transactions["amount_inr"] <= 0
]

print(f"\nInvalid Amount Records: {len(invalid_amount)}")

if len(invalid_amount) == 0:
    print("✓ All transaction amounts are valid.")
else:
    print("⚠ Invalid transaction amounts found!")

# Standardize KYC
investor_transactions["kyc_status"] = (
    investor_transactions["kyc_status"]
    .str.strip()
    .str.upper()
)

print("\nUnique KYC Status Values:")
print(investor_transactions["kyc_status"].unique())

# Validate KYC
valid_kyc = ["VERIFIED", "PENDING"]

invalid_kyc = investor_transactions[
    ~investor_transactions["kyc_status"].isin(valid_kyc)
]

print(f"\nInvalid KYC Records: {len(invalid_kyc)}")

if len(invalid_kyc) == 0:
    print("✓ All KYC values are valid.")
else:
    print("⚠ Invalid KYC values found!")

# Save
investor_transactions.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("✓ Cleaned Investor Transactions saved.")


# ==========================================================
# PIPELINE COMPLETED
# ==========================================================

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("=" * 60)

# ==========================================================
# 03. AUM BY FUND HOUSE
# ==========================================================

print("\n" + "=" * 60)
print("AUM BY FUND HOUSE DATA CLEANING")
print("=" * 60)

aum_data = load_dataset("03_aum_by_fund_house.csv")

print("\n========== AUM BY FUND HOUSE PREVIEW ==========")
print(aum_data.head())

print("\nData Types:")
print(aum_data.dtypes)

print("\nMissing Values:")
print(aum_data.isnull().sum())

print("\nDuplicate Rows:")
print(aum_data.duplicated().sum())

print("\n========== CLEANING AUM BY FUND HOUSE ==========")

# Convert date
aum_data["date"] = pd.to_datetime(aum_data["date"])
print("✓ Date converted to datetime")

# Standardize fund house names
aum_data["fund_house"] = (
    aum_data["fund_house"]
    .str.strip()
    .str.title()
)
print("✓ Fund house names standardized")

# Validate AUM
invalid_aum = aum_data[aum_data["aum_crore"] <= 0]

print(f"\nInvalid AUM Records: {len(invalid_aum)}")

if len(invalid_aum) == 0:
    print("✓ All AUM values are valid.")
else:
    print("⚠ Invalid AUM values found!")

# Validate scheme count
invalid_scheme = aum_data[aum_data["num_schemes"] <= 0]

print(f"Invalid Scheme Records: {len(invalid_scheme)}")

if len(invalid_scheme) == 0:
    print("✓ All scheme counts are valid.")
else:
    print("⚠ Invalid scheme counts found!")

# Sort dataset
aum_data = aum_data.sort_values(
    by=["date", "fund_house"]
)

print("✓ Dataset sorted successfully")

# Save cleaned dataset
aum_data.to_csv(
    "data/processed/03_aum_by_fund_house_cleaned.csv",
    index=False
)

print("✓ Cleaned AUM dataset saved.")

print("\n" + "=" * 60)
print("AUM DATA CLEANING COMPLETED")
print("=" * 60)
# ==========================================================
# 04. MONTHLY SIP INFLOWS
# ==========================================================
print("\n" + "=" * 60)
print("MONTHLY SIP INFLOWS DATA CLEANING")
print("=" * 60)
sip_data = load_dataset("04_monthly_sip_inflows.csv")

print("\n========== CLEANING MONTHLY SIP INFLOWS ==========")

# Convert month to datetime
sip_data["month"] = pd.to_datetime(
    sip_data["month"],
    format="%Y-%m"
)

print("✓ Month converted to datetime")

# Sort by month
sip_data = sip_data.sort_values("month")

print("✓ Dataset sorted successfully")

# Fill missing YoY growth values
sip_data["yoy_growth_pct"] = (
    sip_data["yoy_growth_pct"]
    .fillna(0)
)

print("✓ Missing YoY Growth values filled")

# Validate SIP inflow
invalid_sip = sip_data[
    sip_data["sip_inflow_crore"] <= 0
]

print(f"\nInvalid SIP Inflow Records: {len(invalid_sip)}")

if len(invalid_sip) == 0:
    print("✓ All SIP inflow values are valid.")
else:
    print("⚠ Invalid SIP inflow values found!")

# Validate Active SIP Accounts
invalid_accounts = sip_data[
    sip_data["active_sip_accounts_crore"] <= 0
]

print(f"Invalid Active SIP Account Records: {len(invalid_accounts)}")

if len(invalid_accounts) == 0:
    print("✓ All Active SIP Account values are valid.")
else:
    print("⚠ Invalid Active SIP Account values found!")

# Save cleaned dataset
sip_data.to_csv(
    "data/processed/04_monthly_sip_inflows_cleaned.csv",
    index=False
)

print("✓ Cleaned Monthly SIP Inflows dataset saved.")

print("\n" + "=" * 60)
print("MONTHLY SIP INFLOWS CLEANING COMPLETED")
print("=" * 60)

# ==========================================================
# 05. CATEGORY INFLOWS
# ==========================================================

print("\n" + "=" * 60)
print("CATEGORY INFLOWS DATA CLEANING")
print("=" * 60)

category_data = load_dataset("05_category_inflows.csv")

print("\n========== CLEANING CATEGORY INFLOWS ==========")

# Convert month to datetime
category_data["month"] = pd.to_datetime(
    category_data["month"],
    format="%Y-%m"
)

print("✓ Month converted to datetime")

# Standardize category names
category_data["category"] = (
    category_data["category"]
    .str.strip()
    .str.title()
)

print("✓ Category names standardized")

# Validate net inflow
invalid_inflow = category_data[
    category_data["net_inflow_crore"] < 0
]

print(f"\nInvalid Net Inflow Records: {len(invalid_inflow)}")

if len(invalid_inflow) == 0:
    print("✓ All net inflow values are valid.")
else:
    print("⚠ Invalid net inflow values found!")

# Sort dataset
category_data = category_data.sort_values(
    by=["month", "category"]
)

print("✓ Dataset sorted successfully")

# Save cleaned dataset
category_data.to_csv(
    "data/processed/05_category_inflows_cleaned.csv",
    index=False
)

print("✓ Cleaned Category Inflows dataset saved.")

print("\n" + "=" * 60)
print("CATEGORY INFLOWS CLEANING COMPLETED")
print("=" * 60)

print("\n" + "=" * 60)
print("INDUSTRY FOLIO COUNT DATA CLEANING")
print("=" * 60)

industry_data = load_dataset("06_industry_folio_count.csv")

print("\n========== CLEANING INDUSTRY FOLIO COUNT ==========")

# Convert month to datetime
industry_data["month"] = pd.to_datetime(industry_data["month"])
print("✓ Month converted to datetime")

# Validate Total Folios
invalid_total = industry_data[
    industry_data["total_folios_crore"] <= 0
]

print(f"\nInvalid Total Folio Records: {len(invalid_total)}")

if len(invalid_total) == 0:
    print("✓ All Total Folio values are valid.")
else:
    print("⚠ Invalid Total Folio values found!")

# Validate Equity Folios
invalid_equity = industry_data[
    industry_data["equity_folios_crore"] <= 0
]

print(f"Invalid Equity Folio Records: {len(invalid_equity)}")

if len(invalid_equity) == 0:
    print("✓ All Equity Folio values are valid.")
else:
    print("⚠ Invalid Equity Folio values found!")

# Validate Debt Folios
invalid_debt = industry_data[
    industry_data["debt_folios_crore"] <= 0
]

print(f"Invalid Debt Folio Records: {len(invalid_debt)}")

if len(invalid_debt) == 0:
    print("✓ All Debt Folio values are valid.")
else:
    print("⚠ Invalid Debt Folio values found!")

# Validate Hybrid Folios
invalid_hybrid = industry_data[
    industry_data["hybrid_folios_crore"] <= 0
]

print(f"Invalid Hybrid Folio Records: {len(invalid_hybrid)}")

if len(invalid_hybrid) == 0:
    print("✓ All Hybrid Folio values are valid.")
else:
    print("⚠ Invalid Hybrid Folio values found!")

# Validate Others Folios
invalid_others = industry_data[
    industry_data["others_folios_crore"] <= 0
]

print(f"Invalid Others Folio Records: {len(invalid_others)}")

if len(invalid_others) == 0:
    print("✓ All Others Folio values are valid.")
else:
    print("⚠ Invalid Others Folio values found!")

# Sort dataset
industry_data = industry_data.sort_values("month")
print("✓ Dataset sorted successfully")

# Save cleaned dataset
industry_data.to_csv(
    "data/processed/06_industry_folio_count_cleaned.csv",
    index=False
)

print("✓ Cleaned Industry Folio Count dataset saved.")

print("\n" + "=" * 60)
print("INDUSTRY FOLIO COUNT CLEANING COMPLETED")
print("=" * 60)

# ==========================================================
# 07. SCHEME PERFORMANCE
# ==========================================================

print("\n" + "=" * 60)
print("SCHEME PERFORMANCE DATA CLEANING")
print("=" * 60)

scheme_data = load_dataset("07_scheme_performance.csv")

print("\n========== SCHEME PERFORMANCE PREVIEW ==========")
print(scheme_data.head())

print("\nData Types:")
print(scheme_data.dtypes)

print("\nMissing Values:")
print(scheme_data.isnull().sum())

print("\nDuplicate Rows:")
print(scheme_data.duplicated().sum())

print("\n========== CLEANING SCHEME PERFORMANCE ==========")

# ----------------------------------------------------------
# Standardize text columns
# ----------------------------------------------------------

scheme_data["scheme_name"] = (
    scheme_data["scheme_name"]
    .astype(str)
    .str.strip()
)

scheme_data["fund_house"] = (
    scheme_data["fund_house"]
    .astype(str)
    .str.strip()
    .str.title()
)

scheme_data["category"] = (
    scheme_data["category"]
    .astype(str)
    .str.strip()
    .str.title()
)

scheme_data["plan"] = (
    scheme_data["plan"]
    .astype(str)
    .str.strip()
    .str.title()
)

scheme_data["risk_grade"] = (
    scheme_data["risk_grade"]
    .astype(str)
    .str.strip()
    .str.title()
)

print("✓ Text columns standardized")

# ----------------------------------------------------------
# Validate Returns
# ----------------------------------------------------------

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for col in return_columns:

    invalid = scheme_data[
        (scheme_data[col] < -100) |
        (scheme_data[col] > 1000)
    ]

    print(f"\nInvalid {col}: {len(invalid)}")

    if len(invalid) == 0:
        print(f"✓ {col} values are valid.")
    else:
        print(f"⚠ Invalid values found in {col}")

# ----------------------------------------------------------
# Validate Expense Ratio
# ----------------------------------------------------------

invalid_expense = scheme_data[
    scheme_data["expense_ratio_pct"] < 0
]

print(f"\nInvalid Expense Ratio Records: {len(invalid_expense)}")

if len(invalid_expense) == 0:
    print("✓ Expense Ratio values are valid.")
else:
    print("⚠ Invalid Expense Ratio values found.")

# ----------------------------------------------------------
# Validate AUM
# ----------------------------------------------------------

invalid_aum = scheme_data[
    scheme_data["aum_crore"] <= 0
]

print(f"\nInvalid AUM Records: {len(invalid_aum)}")

if len(invalid_aum) == 0:
    print("✓ AUM values are valid.")
else:
    print("⚠ Invalid AUM values found.")

# ----------------------------------------------------------
# Validate Morningstar Rating
# ----------------------------------------------------------

invalid_rating = scheme_data[
    (scheme_data["morningstar_rating"] < 1) |
    (scheme_data["morningstar_rating"] > 5)
]

print(f"\nInvalid Morningstar Rating Records: {len(invalid_rating)}")

if len(invalid_rating) == 0:
    print("✓ Morningstar ratings are valid.")
else:
    print("⚠ Invalid Morningstar ratings found.")

# ----------------------------------------------------------
# Sort Dataset
# ----------------------------------------------------------

scheme_data = scheme_data.sort_values(
    by=["fund_house", "scheme_name"]
)

print("✓ Dataset sorted successfully")

# ----------------------------------------------------------
# Save Cleaned Dataset
# ----------------------------------------------------------

scheme_data.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("✓ Cleaned Scheme Performance dataset saved.")

print("\n" + "=" * 60)
print("SCHEME PERFORMANCE CLEANING COMPLETED")
print("=" * 60)

print("\n" + "=" * 60)
print("PORTFOLIO HOLDINGS DATA CLEANING")
print("=" * 60)

portfolio_data = load_dataset("09_portfolio_holdings.csv")

# ==========================================================
# CLEANING PORTFOLIO HOLDINGS
# ==========================================================

print("\n========== CLEANING PORTFOLIO HOLDINGS ==========")

# Convert portfolio date to datetime
portfolio_data["portfolio_date"] = pd.to_datetime(
    portfolio_data["portfolio_date"]
)

print("✓ Portfolio date converted to datetime")

# Standardize text columns
portfolio_data["stock_symbol"] = (
    portfolio_data["stock_symbol"]
    .str.strip()
    .str.upper()
)

portfolio_data["stock_name"] = (
    portfolio_data["stock_name"]
    .str.strip()
    .str.title()
)

portfolio_data["sector"] = (
    portfolio_data["sector"]
    .str.strip()
    .str.title()
)

print("✓ Text columns standardized")

# ----------------------------------------------------------
# Validate Weight %
# ----------------------------------------------------------

invalid_weight = portfolio_data[
    (portfolio_data["weight_pct"] < 0) |
    (portfolio_data["weight_pct"] > 100)
]

print(f"\nInvalid Weight Records: {len(invalid_weight)}")

if len(invalid_weight) == 0:
    print("✓ All Weight values are valid.")
else:
    print("⚠ Invalid Weight values found!")

# ----------------------------------------------------------
# Validate Market Value
# ----------------------------------------------------------

invalid_market = portfolio_data[
    portfolio_data["market_value_cr"] <= 0
]

print(f"\nInvalid Market Value Records: {len(invalid_market)}")

if len(invalid_market) == 0:
    print("✓ All Market Value values are valid.")
else:
    print("⚠ Invalid Market Value values found!")

# ----------------------------------------------------------
# Validate Current Price
# ----------------------------------------------------------

invalid_price = portfolio_data[
    portfolio_data["current_price_inr"] <= 0
]

print(f"\nInvalid Current Price Records: {len(invalid_price)}")

if len(invalid_price) == 0:
    print("✓ All Current Price values are valid.")
else:
    print("⚠ Invalid Current Price values found!")

# ----------------------------------------------------------
# Sort Dataset
# ----------------------------------------------------------

portfolio_data = portfolio_data.sort_values(
    by=["portfolio_date", "stock_symbol"]
)

print("✓ Dataset sorted successfully")

# ----------------------------------------------------------
# Save Cleaned Dataset
# ----------------------------------------------------------

portfolio_data.to_csv(
    "data/processed/09_portfolio_holdings_cleaned.csv",
    index=False
)

print("✓ Cleaned Portfolio Holdings dataset saved.")

print("\n" + "=" * 60)
print("PORTFOLIO HOLDINGS CLEANING COMPLETED")
print("=" * 60)

# ==========================================================
# 10. BENCHMARK INDICES
# ==========================================================

print("\n" + "=" * 60)
print("BENCHMARK INDICES DATA CLEANING")
print("=" * 60)

benchmark_data = load_dataset("10_benchmark_indices.csv")

print("\n========== BENCHMARK INDICES PREVIEW ==========")
print(benchmark_data.head())

print("\nData Types:")
print(benchmark_data.dtypes)

print("\nMissing Values:")
print(benchmark_data.isnull().sum())

print("\nDuplicate Rows:")
print(benchmark_data.duplicated().sum())

print("\n========== CLEANING BENCHMARK INDICES ==========")

# ----------------------------------------------------------
# Convert Date
# ----------------------------------------------------------

benchmark_data["date"] = pd.to_datetime(
    benchmark_data["date"]
)

print("✓ Date converted to datetime")

# ----------------------------------------------------------
# Standardize Index Names
# ----------------------------------------------------------

benchmark_data["index_name"] = (
    benchmark_data["index_name"]
    .str.strip()
    .str.upper()
)

print("✓ Index names standardized")

# ----------------------------------------------------------
# Validate Close Value
# ----------------------------------------------------------

invalid_close = benchmark_data[
    benchmark_data["close_value"] <= 0
]

print(f"\nInvalid Close Value Records: {len(invalid_close)}")

if len(invalid_close) == 0:
    print("✓ All Close Value records are valid.")
else:
    print("⚠ Invalid Close Value records found!")

# ----------------------------------------------------------
# Sort Dataset
# ----------------------------------------------------------

benchmark_data = benchmark_data.sort_values(
    by=["index_name", "date"]
)

print("✓ Dataset sorted successfully")

# ----------------------------------------------------------
# Save Cleaned Dataset
# ----------------------------------------------------------

benchmark_data.to_csv(
    "data/processed/10_benchmark_indices_cleaned.csv",
    index=False
)

print("✓ Cleaned Benchmark Indices dataset saved.")

print("\n" + "=" * 60)
print("BENCHMARK INDICES CLEANING COMPLETED")
print("=" * 60)

