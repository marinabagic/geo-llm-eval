
import pandas as pd
import geopandas as gpd
import scipy.stats as stats
import matplotlib.pyplot as plt

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Calculate Z-score for EC
geo_df['EC_zscore'] = stats.zscore(geo_df['EC'], nan_policy='omit')

# Filter outliers
outliers = geo_df[(geo_df['EC_zscore'] > 3) | (geo_df['EC_zscore'] < -3)]

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color='lightgrey')
outliers.plot(ax=ax, marker='.', column='EC', legend=True)

# Save plot
plt.savefig('plots/plot11.png')
