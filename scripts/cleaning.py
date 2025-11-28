import pandas as pd

# Load dataset
df = pd.read_csv("../data/raw/online_retail_II(Year 2010-2011).csv")

# Basic cleaning
df = df.drop_duplicates()
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Remove rows with missing key fields
df = df.dropna(subset=["transaction_id", "product", "store"])

# Save cleaned version
df.to_csv("../data/processed/retail_cleaned.csv", index=False)

print("Dataset cleaned and saved.")
