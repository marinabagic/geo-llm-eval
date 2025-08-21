
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')

# Filter the GeoDataFrame for Woodland areas with pH in water < 6
woodland_areas = geo_df[(geo_df['LC'] == 'Woodland') & (geo_df['pH_H2O'] < 6)]

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot the filtered Woodland areas
woodland_areas.plot(ax=ax, marker='.', markersize=1)

# Save the plot
plt.savefig('plots/plot19.png')
