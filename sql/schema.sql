-- ==========================================================
-- DIMENSION TABLE : FUND
-- ==========================================================

CREATE TABLE IF NOT EXISTS dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    plan TEXT,
    risk_grade TEXT,
    morningstar_rating INTEGER
);

-- ==========================================================
-- DIMENSION TABLE : DATE
-- ==========================================================

CREATE TABLE IF NOT EXISTS dim_date (
    date TEXT PRIMARY KEY,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    day INTEGER
);

-- ==========================================================
-- FACT TABLE : NAV
-- ==========================================================

CREATE TABLE IF NOT EXISTS fact_nav (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    date TEXT,
    nav REAL,
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY(date) REFERENCES dim_date(date)
);

-- ==========================================================
-- FACT TABLE : TRANSACTIONS
-- ==========================================================

CREATE TABLE IF NOT EXISTS fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    investor_id INTEGER,
    amfi_code INTEGER,
    transaction_date TEXT,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    kyc_status TEXT,
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

-- ==========================================================
-- FACT TABLE : PERFORMANCE
-- ==========================================================

CREATE TABLE IF NOT EXISTS fact_performance (
    amfi_code INTEGER PRIMARY KEY,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    benchmark_3yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    std_dev_ann_pct REAL,
    max_drawdown_pct REAL,
    expense_ratio_pct REAL,
    aum_crore REAL,
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

-- ==========================================================
-- FACT TABLE : AUM
-- ==========================================================

CREATE TABLE IF NOT EXISTS fact_aum (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    fund_house TEXT,
    aum_crore REAL,
    num_schemes INTEGER
);