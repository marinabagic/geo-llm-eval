
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot the points from geo_df
geo_df.plot(ax=ax, marker='.', markersize=5, column='EC', legend=True)

# Save the plot
plt.savefig('plots/plot8.png')

# Create a boxplot of EC grouped by land use class
plt.figure(figsize=(12, 8))
geo_df.boxplot(column='EC', by='LU', grid=False)
plt.title('Boxplot of EC grouped by Land Use Class')
plt.suptitle('')
plt.xlabel('Land Use Class')
plt.ylabel('EC')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the boxplot
plt.savefig('plots/plot8.png')
