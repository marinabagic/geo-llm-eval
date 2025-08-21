
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the Europe shapefile
europe_gdf = gpd.read_file('europe.gpkg')

# Load the countries shapefile
countries_gdf = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Filter points with pH in CaCl2 > 6
filtered_geo_df = geo_df[geo_df['pH_CaCl2'] > 6]

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot countries
countries_gdf.plot(ax=ax, color='none', edgecolor='black')

# Plot filtered points
filtered_geo_df.plot(ax=ax, marker='.', markersize=5, color='red')

# Save the plot
plt.savefig('plots/plot17.png')
plt.close()
