
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')

# Filter the GeoDataFrame for nitrogen outliers (N > 4)
nitrogen_outliers = geo_df[geo_df['N'] > 4]

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot the nitrogen outliers
nitrogen_outliers.plot(ax=ax, marker='.', color='red')

# Save the plot
plt.savefig('plots/plot25.png')
