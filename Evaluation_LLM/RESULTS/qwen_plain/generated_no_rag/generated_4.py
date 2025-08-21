
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot the points from geo_df
geo_df.plot(ax=ax, marker='.', markersize=1, color='black')

# Save the plot
plt.savefig('plots/plot4.png')

# Plot histogram of phosphorus content with KDE
plt.figure(figsize=(10, 6))
geo_df['P'].plot(kind='hist', bins=30, density=True, alpha=0.6, color='blue', edgecolor='black')
geo_df['P'].plot(kind='kde', color='red')
plt.title('Histogram of Phosphorus Content with KDE')
plt.xlabel('Phosphorus (P)')
plt.ylabel('Density')
plt.savefig('plots/plot4.png')
