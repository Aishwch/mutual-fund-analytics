-- =====================================================
-- Mutual Fund Analytics - Analytical SQL Queries
-- =====================================================

---------------------------------------------------------
-- 1. Top 5 Funds by AUM
---------------------------------------------------------
SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM 07_scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

---------------------------------------------------------
-- 2. Average NAV of each Fund
---------------------------------------------------------
SELECT
    amfi_code,
    ROUND(AVG(nav),2) AS average_nav
FROM 02_nav_history
GROUP BY amfi_code
ORDER BY average_nav DESC;

---------------------------------------------------------
-- 3. Total SIP Inflow
---------------------------------------------------------
SELECT
    SUM(sip_inflow_cr) AS total_sip_inflow
FROM 04_monthly_sip_inflows;

---------------------------------------------------------
-- 4. Transactions by State
---------------------------------------------------------
SELECT
    state,
    SUM(amount) AS total_transaction_amount
FROM 08_investor_transactions
GROUP BY state
ORDER BY total_transaction_amount DESC;

---------------------------------------------------------
-- 5. Funds with Expense Ratio less than 1%
---------------------------------------------------------
SELECT
    scheme_name,
    expense_ratio_pct
FROM 07_scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

---------------------------------------------------------
-- 6. Top Performing Funds (5-Year Return)
---------------------------------------------------------
SELECT
    scheme_name,
    return_5yr_pct
FROM 07_scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

---------------------------------------------------------
-- 7. Average Alpha by Category
---------------------------------------------------------
SELECT
    category,
    ROUND(AVG(alpha),2) AS average_alpha
FROM 07_scheme_performance
GROUP BY category
ORDER BY average_alpha DESC;

---------------------------------------------------------
-- 8. Total AUM by Fund House
---------------------------------------------------------
SELECT
    fund_house,
    SUM(aum_crore) AS total_aum
FROM 03_aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC;

---------------------------------------------------------
-- 9. Monthly Category Inflows
---------------------------------------------------------
SELECT
    month,
    category,
    net_inflow_crore
FROM 05_category_inflows
ORDER BY month;

---------------------------------------------------------
-- 10. Top Portfolio Holdings by Market Value
---------------------------------------------------------
SELECT
    stock_name,
    sector,
    market_value_cr
FROM 09_portfolio_holdings
ORDER BY market_value_cr DESC
LIMIT 10;