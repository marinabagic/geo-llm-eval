
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Filter for July 2018
filtered_df = geo_df[geo_df['SURVEY_DATE'].str.contains('07-18')]

# Load the Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Load the countries shapefile
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color='lightgrey', edgecolor='black')
countries.plot(ax=ax, color='none', edgecolor='black')
filtered_df.plot(ax=ax, column='LC0_Desc', cmap='tab10', markersize=5, marker='.', legend=True)
ax.set_title("Locations Sampled in July 2018, Colored by LC0_Desc")
plt.tight_layout()
plt.savefig('plots/plot33.png')
