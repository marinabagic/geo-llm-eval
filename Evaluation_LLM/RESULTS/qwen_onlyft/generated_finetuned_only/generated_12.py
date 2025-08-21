
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Calculate mean organic carbon
mean_oc = geo_df['OC'].mean()

# Calculate confidence interval
confidence_interval = geo_df['OC'].sem() * 1.96

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color='lightgrey')

# Save plot
plt.savefig('plots/plot12.png')
plt.close()
