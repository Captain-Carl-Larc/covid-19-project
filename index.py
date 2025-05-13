import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
def load_data(filepath):
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    return df

# 2. Clean Data
def clean_data(df, countries, critical_columns):
    df = df[df['location'].isin(countries)]
    df = df.dropna(subset=['date'] + critical_columns)
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = df[numeric_cols].interpolate()
    df['death_rate'] = df['total_deaths'] / df['total_cases']
    return df

# 3. Line Plot Function
def plot_line(df, countries, y_column, title, ylabel):
    plt.figure(figsize=(12, 6))
    for country in countries:
        subset = df[df['location'] == country]
        plt.plot(subset['date'], subset[y_column], label=country)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 4. Bar Chart for Top Countries by Cases
def plot_top_10_countries_by_cases(df):
    latest_df = df.sort_values('date').groupby('location').tail(1)
    latest_df = latest_df[latest_df['continent'].notna()]  # filter continents/aggregates
    top_countries = latest_df.nlargest(10, 'total_cases')

    plt.figure(figsize=(12, 6))
    plt.bar(top_countries['location'], top_countries['total_cases'], color='orange')
    plt.title('Top 10 Countries by Total COVID-19 Cases')
    plt.xlabel('Country')
    plt.ylabel('Total Cases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 5. Correlation Heatmap
def plot_correlation_heatmap(df):
    plt.figure(figsize=(8, 6))
    sns.heatmap(df[['total_cases', 'total_deaths', 'total_vaccinations', 'death_rate']].corr(),
                annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

# 🚀 Run Workflow
# Step 1: Load
df = load_data('owid-covid-data.csv')

# Step 2: Clean
countries = ['Kenya', 'United States', 'India']
critical_columns = ['total_cases', 'total_deaths', 'total_vaccinations']
df_clean = clean_data(df, countries, critical_columns)

# Step 3: Visualizations
plot_line(df_clean, countries, 'total_cases', 'Total COVID-19 Cases Over Time', 'Total Cases')
plot_line(df_clean, countries, 'total_deaths', 'Total COVID-19 Deaths Over Time', 'Total Deaths')
plot_line(df_clean, countries, 'new_cases', 'Daily New COVID-19 Cases', 'New Cases')

# Step 4: Bar Chart
plot_top_10_countries_by_cases(df)

# Step 5: Heatmap
plot_correlation_heatmap(df_clean)
