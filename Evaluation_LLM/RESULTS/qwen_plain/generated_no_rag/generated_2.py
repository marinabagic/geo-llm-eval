
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot the points with average organic carbon content by general land cover type
geo_df.groupby('LC')['OC'].mean().plot(kind='bar', ax=ax, color='blue', alpha=0.5)

# Save the plot
plt.savefig('plots/plot2.png')
