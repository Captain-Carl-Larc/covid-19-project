import pandas as pd
import plotly.express as px

def plot_vaccination_choropleth(data_path):
    # Load dataset
    df = pd.read_csv(data_path)
    df['date'] = pd.to_datetime(df['date'])

    # Get latest data per country
    latest_data = df.sort_values('date').groupby('location').tail(1)
    latest_data = latest_data[latest_data['iso_code'].str.len() == 3]
    latest_data = latest_data[latest_data['continent'].notna()]

    # Filter relevant columns
    choropleth_df = latest_data[['iso_code', 'location', 'people_fully_vaccinated_per_hundred']].dropna()

    # Plot choropleth
    fig = px.choropleth(
        choropleth_df,
        locations='iso_code',
        color='people_fully_vaccinated_per_hundred',
        hover_name='location',
        color_continuous_scale='Greens',
        title='Global COVID-19 Vaccination Rates (People Fully Vaccinated per 100)',
        labels={'people_fully_vaccinated_per_hundred': 'Fully Vaccinated per 100 People'}
    )
    fig.update_layout(geo=dict(showframe=False, showcoastlines=False))
    fig.show()


plot_vaccination_choropleth('owid-covid-data.csv')
