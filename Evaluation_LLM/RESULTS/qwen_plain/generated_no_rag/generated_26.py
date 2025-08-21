
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot the points where organic carbon content is available
geo_df[geo_df['OC'].notna()].plot(ax=ax, marker='.', markersize=5, color='red')

# Save the plot
plt.savefig('plots/plot26.png')
