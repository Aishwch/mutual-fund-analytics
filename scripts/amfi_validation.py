import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

# Get unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

print("\nTotal AMFI Codes in Fund Master:", len(fund_codes))
print("Total AMFI Codes in NAV History:", len(nav_codes))

# Check for missing AMFI codes
missing_codes = fund_codes - nav_codes

print("\n" + "=" * 60)
print("VALIDATION RESULT")
print("=" * 60)

if len(missing_codes) == 0:
    print("Success! Every AMFI code in Fund Master exists in NAV History.")
else:
    print("Missing AMFI Codes:")
    print(sorted(missing_codes))