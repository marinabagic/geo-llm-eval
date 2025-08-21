
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the Europe shapefile
europe_gdf = gpd.read_file('europe.gpkg')

# Load the countries shapefile
countries_gdf = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Filter countries to only include those in Europe
european_countries_gdf = countries_gdf[countries_gdf['CONTINENT'] == 'Europe']

# Load the soil samples GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot Europe shapefile
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot European countries
european_countries_gdf.plot(ax=ax, edgecolor='black', facecolor='none')

# Plot soil sample points
geo_df.plot(ax=ax, marker='.', markersize=5, color='red')

# Save the plot
plt.savefig('plots/plot16.png')
