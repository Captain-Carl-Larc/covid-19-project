import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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


# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter countries of interest
countries = ['Kenya', 'United States', 'India']
df_filtered = df[df['location'].isin(countries)]

# Drop rows with missing date or critical values
critical_columns = ['total_cases', 'total_deaths', 'total_vaccinations']
df_filtered = df_filtered.dropna(subset=['date'] + critical_columns, how='any')

# Interpolate missing numeric values
numeric_cols = df_filtered.select_dtypes(include=['float64', 'int64']).columns
df_filtered[numeric_cols] = df_filtered[numeric_cols].interpolate()