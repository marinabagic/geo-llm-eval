
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Calculate Z-score for EC
geo_df['EC_ZScore'] = (geo_df['EC'] - geo_df['EC'].mean()) / geo_df['EC'].std()

# Identify outliers
outliers = geo_df[np.abs(geo_df['EC_ZScore']) > 3]

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color='lightgrey')
outliers.plot(ax=ax, column='EC', marker='.', legend=True)

# Save plot
plt.savefig('plots/plot11.png')
plt.close()
