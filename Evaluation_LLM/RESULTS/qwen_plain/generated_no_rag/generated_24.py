
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')

# Plot the heatmap of pH values in water
geo_df.plot(ax=ax, column='pH_H2O', legend=True, cmap='viridis', markersize=5, marker='.')

# Save the plot
plt.savefig('plots/plot24.png')
plt.close(fig)
