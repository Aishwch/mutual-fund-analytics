import os
import pandas as pd

RAW_DATA_PATH = "data/raw"

csv_files = sorted([
    file for file in os.listdir(RAW_DATA_PATH)
    if file.endswith(".csv")
])

print("=" * 60)
print("Mutual Fund Analytics - Data Ingestion")
print("=" * 60)
print(f"Total CSV files found: {len(csv_files)}\n")

for file in csv_files:
    file_path = os.path.join(RAW_DATA_PATH, file)

    print("=" * 60)
    print(f"Reading: {file}")

    df = pd.read_csv(file_path)

    print(f"Shape: {df.shape}")

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\n")