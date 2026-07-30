import pandas as pd

# Load the fund master dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("FUND MASTER DATASET")
print("=" * 60)

# Shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumns:")
for col in df.columns:
    print("-", col)

# First 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Total number of schemes
print("\nTotal Schemes:")
print(len(df))

# Unique Fund Houses
print("\n" + "=" * 60)
print("UNIQUE FUND HOUSES")
print("=" * 60)

print(df["fund_house"].unique())
print("Total Fund Houses:", df["fund_house"].nunique())


# Unique Categories
print("\n" + "=" * 60)
print("UNIQUE CATEGORIES")
print("=" * 60)

print(df["category"].unique())
print("Total Categories:", df["category"].nunique())


# Unique Sub-Categories
print("\n" + "=" * 60)
print("UNIQUE SUB-CATEGORIES")
print("=" * 60)

print(df["sub_category"].unique())
print("Total Sub-Categories:", df["sub_category"].nunique())


# Unique Risk Categories
print("\n" + "=" * 60)
print("RISK CATEGORIES")
print("=" * 60)

print(df["risk_category"].unique())
print("Total Risk Categories:", df["risk_category"].nunique())


# AMFI Code Structure
print("\n" + "=" * 60)
print("AMFI CODE SAMPLE")
print("=" * 60)

print(df["amfi_code"].head(10))