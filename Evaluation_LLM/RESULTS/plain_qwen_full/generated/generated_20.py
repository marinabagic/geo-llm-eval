
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_gdf = gpd.read_file("europe.gpkg")
countries_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter the points where organic carbon content > 20 in Grassland or Woodland
filtered_points = geo_df[(geo_df['OC'] > 20) & (geo_df['LC'].isin(['Grassland', 'Woodland']))]

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot countries
countries_gdf.plot(ax=ax, edgecolor='black', facecolor='none')

# Plot filtered points
filtered_points.plot(ax=ax, marker='.', color='red')

# Save the plot
plt.savefig('plots/plot20.png')
plt.close(fig)
