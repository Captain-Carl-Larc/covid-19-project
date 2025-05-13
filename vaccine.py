# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Reload the dataset
vacc_df = pd.read_csv("vaccinations.csv")
vacc_df['date'] = pd.to_datetime(vacc_df['date'])

# Define countries of interest
countries = ['Kenya', 'United States', 'India']

# Filter data for selected countries and drop rows with missing values in key columns
vacc_filtered = vacc_df[vacc_df['location'].isin(countries)]
vacc_filtered = vacc_filtered.dropna(subset=['date', 'total_vaccinations_per_hundred'])

# Plot cumulative vaccinations over time for selected countries
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = vacc_filtered[vacc_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations_per_hundred'], label=country)
plt.title('COVID-19 Vaccination Progress Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations per 100 People')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
