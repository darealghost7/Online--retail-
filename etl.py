

import pandas as pd
import os

# Get the folder where etl.py is located
folder = os.path.dirname(os.path.abspath(__file__))

# 1. EXTRACT: Read the CSV file
print("Starting Retail ETL Project...")

file_path = os.path.join(folder, "online_retail_II.csv")

df = pd.read_csv(file_path)

print("\nData extracted successfully!")
print("Original dataset shape:", df.shape)

# 2. INSPECT: Check the data
print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

# 3. TRANSFORM: Clean the data

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing descriptions using matching stock codes
description_map = (
    df.dropna(subset=["Description"])
      .drop_duplicates("StockCode")
      .set_index("StockCode")["Description"]
)

df["Description"] = df["Description"].fillna(
    df["StockCode"].map(description_map)
)

# Fill any remaining missing descriptions
df["Description"] = df["Description"].fillna("Unknown")

print("\nData cleaned successfully!")
print("Cleaned dataset shape:", df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# 4. LOAD: Save the cleaned dataset
output_path = os.path.join(folder, "online_retail_cleaned.csv")

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print("File location:", output_path)
print("ETL process completed!")
