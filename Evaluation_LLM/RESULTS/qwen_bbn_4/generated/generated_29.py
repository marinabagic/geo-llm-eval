
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Calculate the carbon to nitrogen ratio
geo_df['C_N_ratio'] = geo_df['CaCO3'] / geo_df['N']

# Filter points where the carbon to nitrogen ratio is greater than 10
filtered_df = geo_df[geo_df['C_N_ratio'] > 10]

# Load the Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Load the countries shapefile
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color='lightgrey', edgecolor='black')
countries.plot(ax=ax, color='none', edgecolor='black')
filtered_df.plot(ax=ax, marker='.', color='red', markersize=5)

ax.set_title("Points with Carbon to Nitrogen Ratio > 10 in Europe")
plt.tight_layout()
plt.savefig('plots/plot29.png')
