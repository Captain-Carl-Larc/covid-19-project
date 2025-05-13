import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and prepare data
df = pd.read_csv('owid-covid-data.csv')
df['date'] = pd.to_datetime(df['date'])
countries = ['Kenya', 'United States', 'India']
df_filtered = df[df['location'].isin(countries)]
critical_columns = ['total_cases', 'total_deaths', 'total_vaccinations']
df_filtered = df_filtered.dropna(subset=['date'] + critical_columns)
numeric_cols = df_filtered.select_dtypes(include=['float64', 'int64']).columns
df_filtered[numeric_cols] = df_filtered[numeric_cols].interpolate()

# Add death rate column
df_filtered['death_rate'] = df_filtered['total_deaths'] / df_filtered['total_cases']