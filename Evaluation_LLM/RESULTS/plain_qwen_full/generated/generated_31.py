
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_gdf = gpd.read_file("europe.gpkg")
countries_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter points in Croatia where 'OC' is below 20
croatia_points = geo_df[(geo_df['NUTS_0'] == 'HR') & (geo_df['OC'] < 20)]

# Plot Europe shapefile
ax = europe_gdf.plot(color='lightgrey', figsize=(10, 10))

# Plot countries shapefile
countries_gdf.plot(ax=ax, edgecolor='black', facecolor='none')

# Plot points in Croatia
croatia_points.plot(ax=ax, marker='.', color='red')

# Save the plot
plt.savefig('plots/plot31.png')
