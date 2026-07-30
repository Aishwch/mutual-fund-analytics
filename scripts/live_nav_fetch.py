import requests
import pandas as pd

SCHEME_CODE = "125497"   # HDFC Top 100 Direct

url = f"https://api.mfapi.in/mf/{SCHEME_CODE}"

print("=" * 60)
print("Fetching Live NAV...")
print("=" * 60)

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    print("\nScheme Name:")
    print(data["meta"]["scheme_name"])

    nav_df = pd.DataFrame(data["data"])

    print("\nLatest 5 NAV Records:\n")
    print(nav_df.head())

    output_file = "data/raw/live_nav.csv"

    nav_df.to_csv(output_file, index=False)

    print("\nLive NAV saved successfully!")
    print(f"Saved to: {output_file}")

else:
    print("Failed to fetch data.")