
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter geo_df for July 2018
geo_df['SURVEY_DATE'] = pd.to_datetime(geo_df['SURVEY_DATE'], format='%d-%m-%y')
july_2018_df = geo_df[geo_df['SURVEY_DATE'].dt.month == 7]

# Plot Europe
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')

# Plot countries
countries_df[countries_df['CONTINENT'] == 'Europe'].plot(ax=ax, color='white', edgecolor='black')

# Plot points with different colors based on LC0_Desc
july_2018_df.plot(ax=ax, column='LC0_Desc', legend=True, markersize=5, cmap='tab10')

# Set title and save plot
ax.set_title("July 2018 Soil Samples by Land Cover Type")
plt.savefig('plots/plot33.png', dpi=300)
plt.close()
