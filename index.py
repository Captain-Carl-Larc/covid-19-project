import pandas as pd

# Load the dataset
df = pd.read_csv("owid-covid-data.csv")

# View all columns
print("🔑 Columns:")
print(df.columns)

# Preview the first 5 rows
print("\n👀 Preview:")
print(df.head())

# Check for missing values
print("\n❗ Missing Values:")
print(df.isnull().sum().sort_values(ascending=False))
