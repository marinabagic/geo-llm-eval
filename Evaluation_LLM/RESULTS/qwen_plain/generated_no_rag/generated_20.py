
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')

# Filter the points where organic carbon content > 20 in Grassland or Woodland
filtered_points = geo_df[(geo_df['OC'] > 20) & (geo_df['LC'].isin(['Grassland', 'Woodland']))]

# Plot the Europe shapefile
europe_gdf.plot(color='lightgrey', figsize=(10, 10))

# Plot the filtered points
filtered_points.plot(ax=plt.gca(), marker='.', color='red')

# Save the plot
plt.savefig('plots/plot20.png')
