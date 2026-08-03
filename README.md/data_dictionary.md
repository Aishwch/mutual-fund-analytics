# Mutual Fund Analytics - Data Dictionary

## Overview

This document describes all datasets used in the Mutual Fund Analytics project.

---

## 01_fund_master

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Unique fund identifier |
| scheme_name | Text | Mutual fund scheme name |
| fund_house | Text | Asset management company |
| category | Text | Fund category |
| plan | Text | Regular/Direct plan |

---

## 02_nav_history

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Fund ID |
| date | Date | NAV date |
| nav | Decimal | Net Asset Value |

---

## 03_aum_by_fund_house

| Column | Data Type | Description |
|---------|-----------|-------------|
| fund_house | Text | Fund house name |
| month | Date | Reporting month |
| aum_crore | Decimal | Assets Under Management (₹ Crore) |

---

## 04_monthly_sip_inflows

| Column | Data Type | Description |
|---------|-----------|-------------|
| month | Date | Reporting month |
| sip_inflow_cr | Decimal | SIP inflow (₹ Crore) |
| active_sip_accounts | Integer | Active SIP accounts |

---

## 05_category_inflows

| Column | Data Type | Description |
|---------|-----------|-------------|
| month | Date | Reporting month |
| category | Text | Mutual fund category |
| net_inflow_crore | Decimal | Net inflow |

---

## 06_industry_folio_count

| Column | Data Type | Description |
|---------|-----------|-------------|
| month | Date | Reporting month |
| total_folios_crore | Decimal | Total folios |
| equity_folios_crore | Decimal | Equity folios |
| debt_folios_crore | Decimal | Debt folios |
| hybrid_folios_crore | Decimal | Hybrid folios |
| others_folios_crore | Decimal | Other folios |

---

## 07_scheme_performance

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Fund ID |
| scheme_name | Text | Scheme name |
| fund_house | Text | Fund house |
| category | Text | Fund category |
| return_1yr_pct | Decimal | 1-year return |
| return_3yr_pct | Decimal | 3-year return |
| return_5yr_pct | Decimal | 5-year return |
| expense_ratio_pct | Decimal | Expense ratio |
| aum_crore | Decimal | AUM |
| morningstar_rating | Integer | Morningstar rating |

---

## 08_investor_transactions

| Column | Data Type | Description |
|---------|-----------|-------------|
| transaction_id | Integer | Transaction ID |
| state | Text | Investor state |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount | Decimal | Transaction amount |
| transaction_date | Date | Transaction date |

---

## 09_portfolio_holdings

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Fund ID |
| stock_symbol | Text | Stock symbol |
| stock_name | Text | Company name |
| sector | Text | Sector |
| weight_pct | Decimal | Portfolio weight (%) |
| market_value_cr | Decimal | Market value (₹ Crore) |
| current_price_inr | Decimal | Current stock price |
| portfolio_date | Date | Portfolio date |

---

## 10_benchmark_indices

| Column | Data Type | Description |
|---------|-----------|-------------|
| date | Date | Trading date |
| index_name | Text | Benchmark index |
| close_value | Decimal | Closing index value |

---

# Database

SQLite

---

# Source

Bluestock Mutual Fund Analytics Capstone Dataset