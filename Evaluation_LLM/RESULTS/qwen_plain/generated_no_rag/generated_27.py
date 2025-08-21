
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Filter the geo_df for grassland and cropland
grassland_df = geo_df[geo_df['LC'] == 'Grassland']
cropland_df = geo_df[geo_df['LC'] == 'Cropland']

# Plot grassland and cropland locations
grassland_df.plot(ax=ax, marker='.', color='green', label='Grassland')
cropland_df.plot(ax=ax, marker='.', color='brown', label='Cropland')

# Add legend and save the plot
ax.legend()
plt.savefig('plots/plot27.png')
