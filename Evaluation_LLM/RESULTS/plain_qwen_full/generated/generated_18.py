
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the Europe shapefile
europe_gdf = gpd.read_file('europe.gpkg')

# Load the countries shapefile
countries_gdf = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Filter the GeoDataFrame for Woodland areas
woodland_areas = geo_df[geo_df['LC0_Desc'] == 'Woodland']

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot countries shapefile
countries_gdf.plot(ax=ax, color='none', edgecolor='black')

# Plot Woodland areas
woodland_areas.plot(ax=ax, marker='.', markersize=1)

# Save the plot
plt.savefig('plots/plot18.png')
