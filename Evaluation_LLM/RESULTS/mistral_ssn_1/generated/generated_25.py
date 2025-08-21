
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Load the Europe shapefile
europe_shapefile = gpd.read_file('europe.gpkg')

# Set marker and figsize for the plot
plt.figure(figsize=(10,10))

# Plot Europe shapefile with lightgrey color
europe_shapefile.plot(color='lightgrey', marker='.', alpha=0.5)

# Plot GeoDataFrame with nitrogen outliers (N > 4)
outliers = geo_df[geo_df['N'] > 4]
outliers.plot(marker='.', markersize=10, color='red')

# Save the plot as png file in the 'plots' directory
plt.savefig('plots/nitrogen_outliers.png')
