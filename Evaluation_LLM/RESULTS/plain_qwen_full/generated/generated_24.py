
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the Europe shapefile
europe_gdf = gpd.read_file('europe.gpkg')

# Load the countries shapefile
countries_gdf = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Filter countries to only include those in Europe
european_countries = countries_gdf[countries_gdf['CONTINENT'] == 'Europe']

# Load the GeoDataFrame with data points
geo_df = gpd.read_file('geo_df.gpkg')

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot countries
european_countries.plot(ax=ax, edgecolor='black', facecolor='none')

# Plot data points with heatmap of pH values in water
geo_df.plot(ax=ax, x='TH_LONG', y='TH_LAT', kind='scatter', c='pH_H2O', cmap='viridis', marker='.', s=5)

# Save the plot
plt.savefig('plots/plot24.png')
