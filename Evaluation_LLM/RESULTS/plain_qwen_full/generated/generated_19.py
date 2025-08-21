
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the Europe shapefile
europe_gdf = gpd.read_file('europe.gpkg')

# Load the countries shapefile
countries_gdf = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Filter the GeoDataFrame for Woodland areas with pH in water < 6
woodland_ph_filtered = geo_df[(geo_df['LC0_Desc'] == 'Woodland') & (geo_df['pH_H2O'] < 6)]

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot countries shapefile
countries_gdf.plot(ax=ax, color='none', edgecolor='black')

# Plot filtered Woodland areas
woodland_ph_filtered.plot(ax=ax, marker='.', color='green')

# Save the plot
plt.savefig('plots/plot19.png')
