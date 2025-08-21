
import geopandas as gpd
import matplotlib.pyplot as plt

# Read the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Calculate the 90th percentile of K values
top_10_percentile = geo_df['K'].quantile(0.90)

# Filter the points with K values above the 90th percentile
top_k_points = geo_df[geo_df['K'] > top_10_percentile]

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey', edgecolor='black')
top_k_points.plot(ax=ax, marker='.', color='red', markersize=5)

# Save the plot
plt.savefig('plots/plot21.png')
