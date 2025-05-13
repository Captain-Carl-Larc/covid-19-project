# Re-import required libraries after environment reset
import pandas as pd

# Reload the dataset
df = pd.read_csv('owid-covid-data.csv')

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

# Display cleaned data sample
print(df_filtered.head())
