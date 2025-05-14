import pandas as pd

df = pd.read_csv("Covid Data.csv")
df.head()

print(df.columns)
print(df.isnull().sum())

df['date'] = pd.to_datetime(df['date'])

countries = ['Kenya', 'United States', 'India']
df_countries = df[df['location'].isin(countries)]

df_countries = df_countries.dropna(subset=['total_cases', 'total_deaths', 'total_vaccinations'])

df_countries.fillna(0, inplace=True)


import matplotlib.pyplot as plt

for country in countries:
    df_country = df_countries[df_countries['location'] == country]
    plt.plot(df_country['date'], df_country['total_cases'], label=country)

plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.show()

df_countries['death_rate'] = df_countries['total_deaths'] / df_countries['total_cases']

for country in countries:
    df_country = df_countries[df_countries['location'] == country]
    plt.plot(df_country['date'], df_country['total_vaccinations'], label=country)

plt.title('Total Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.show()

import plotly.express as px

latest_date = df['date'].max()
df_latest = df[df['date'] == latest_date]

fig = px.choropleth(df_latest,
                    locations="iso_code",
                    color="total_cases",
                    hover_name="location",
                    color_continuous_scale="Reds",
                    title="Global COVID-19 Cases")
fig.show()



