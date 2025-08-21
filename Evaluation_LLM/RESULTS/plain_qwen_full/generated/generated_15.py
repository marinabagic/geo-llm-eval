
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_gdf = gpd.read_file("europe.gpkg")
countries_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter countries within Europe
europe_countries = countries_gdf[countries_gdf['ISO_A2'].isin(europe_gdf['NUTS_0'])]

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot countries within Europe
europe_countries.plot(ax=ax, edgecolor='black', facecolor='none')

# Plot sampling points
geo_df.plot(ax=ax, x='TH_LONG', y='TH_LAT', marker='.', markersize=1, color='red')

# Save the plot
plt.savefig('plots/plot15.png')
