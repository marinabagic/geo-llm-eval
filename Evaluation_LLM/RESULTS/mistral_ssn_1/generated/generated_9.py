
import pandas as pd
import geopandas as gpd

# Read the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Read the Europe shapefile
europe_shp = gpd.read_file('europe.gpkg')

# Set marker and figsize for plotting
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))

# Plot Europe shapefile with light grey color
europe_shp.plot(color='lightgrey', marker='.', alpha=0.5)

# Plot GeoDataFrame
geo_df.plot(marker='.', alpha=1.0)

# Save the plot as png file in the 'plots' directory
import os
plt.savefig('plots/europe_and_data.png')

# Analyze if organic carbon content differs by land cover using ANOVA
from scipy.stats import f_oneway

# Assuming 'OC' is the column for organic carbon content
oc_values = geo_df['OC'].dropna()

# Group data by land cover (LC)
grouped_data = geo_df.groupby('LC')['OC'].mean()

# Perform ANOVA test
f_value, p_value, _, _ = f_oneway(*grouped_data.values())

print("F-value:", f_value)
print("P-value:", p_value)
