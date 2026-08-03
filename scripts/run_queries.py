import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("sql/bluestock_mf.db")
cursor = conn.cursor()

queries = {
    "Top 5 Funds by AUM": """
        SELECT scheme_name, fund_house, aum_crore
        FROM "07_scheme_performance"
        ORDER BY aum_crore DESC
        LIMIT 5;
    """,

    "Average NAV by Fund": """
        SELECT amfi_code, ROUND(AVG(nav),2)
        FROM "02_nav_history"
        GROUP BY amfi_code
        LIMIT 10;
    """,

    "Transactions by State": """
        SELECT state, ROUND(SUM(amount_inr),2)
        FROM "08_investor_transactions"
        GROUP BY state
        ORDER BY SUM(amount_inr) DESC;
    """,

    "Total SIP Inflow": """
        SELECT SUM(sip_inflow_crore)
        FROM "04_monthly_sip_inflows";
    """,

    "Funds with Expense Ratio < 1%": """
        SELECT scheme_name, expense_ratio_pct
        FROM "07_scheme_performance"
        WHERE expense_ratio_pct < 1;
    """
}

for title, query in queries.items():
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

conn.close()