
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot the points from geo_df
geo_df.plot(ax=ax, marker='.', markersize=5, color='blue')

# Save the plot
plt.savefig('plots/plot15.png')
