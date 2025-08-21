
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the Europe shapefile
europe_gdf = gpd.read_file('europe.gpkg')

# Load the countries shapefile
countries_gdf = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Filter countries within Europe
european_countries = countries_gdf[countries_gdf['CONTINENT'] == 'Europe']

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot countries within Europe
european_countries.plot(ax=ax, edgecolor='black', facecolor='none')

# Plot sampling locations colored by detailed land cover category
geo_df.plot(ax=ax, column='LC1_Desc', legend=True, markersize=5, marker='.')

# Save the plot
plt.savefig('plots/plot23.png')
