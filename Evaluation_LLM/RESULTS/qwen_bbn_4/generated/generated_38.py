
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Load Europe shapefile
europe_df = gpd.read_file('europe.gpkg')

# Load countries shapefile
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter countries shapefile to only include Europe
europe_countries = countries_df[countries_df['CONTINENT'] == 'Europe']

# Find London's coordinates
london_coords = europe_countries[europe_countries['NAME'] == 'United Kingdom'].centroid.iloc[0]

# Buffer around London for 100 km
buffer_distance = 100000  # 100 km in meters
london_buffer = london_coords.buffer(buffer_distance)

# Filter points within the buffer
points_within_buffer = geo_df[geo_df.geometry.within(london_buffer)]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey', edgecolor='black')
europe_countries.plot(ax=ax, color='none', edgecolor='black')
points_within_buffer.plot(ax=ax, column='LC0_Desc', cmap='tab10', markersize=5, legend=True, marker='.')
ax.set_title('Points within 100 km of London, colored by LC0_Desc')
plt.tight_layout()
plt.savefig('plots/plot38.png')
