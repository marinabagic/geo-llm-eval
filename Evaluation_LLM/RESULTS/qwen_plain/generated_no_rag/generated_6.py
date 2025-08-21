
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')

# Plot the points from geo_df
geo_df.plot(ax=ax, marker='.', markersize=5, alpha=0.5)

# Save the plot
plt.savefig('plots/plot6.png')
plt.close(fig)
