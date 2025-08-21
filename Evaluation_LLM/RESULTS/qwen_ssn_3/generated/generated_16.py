
import geopandas as gpd
import matplotlib.pyplot as plt

# Read the GeoDataFrame and Europe shapefile
geo_df = gpd.read_file('geo_df.gpkg')
europe_shapefile = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile with lightgrey color
fig, ax = plt.subplots(figsize=(10, 10))
europe_shapefile.plot(ax=ax, color='lightgrey', edgecolor='black')

# Plot the soil sample points
geo_df.plot(ax=ax, marker='.', color='blue', markersize=5)

# Save the plot
plt.title('Soil Sample Points on Europe Map')
plt.savefig('plots/plot16.png')
