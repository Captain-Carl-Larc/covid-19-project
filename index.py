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

# Plot total cases over time
plt.figure(figsize=(12, 6))
for country in countries:
    subset = df_filtered[df_filtered['location'] == country]
    plt.plot(subset['date'], subset['total_cases'], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot total deaths over time
plt.figure(figsize=(12, 6))
for country in countries:
    subset = df_filtered[df_filtered['location'] == country]
    plt.plot(subset['date'], subset['total_deaths'], label=country)
plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot daily new cases
plt.figure(figsize=(12, 6))
for country in countries:
    subset = df_filtered[df_filtered['location'] == country]
    plt.plot(subset['date'], subset['new_cases'], label=country)
plt.title("Daily New COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df_filtered[['total_cases', 'total_deaths', 'total_vaccinations', 'death_rate']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()