
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the Europe shapefile
europe_gdf = gpd.read_file('europe.gpkg')

# Load the countries shapefile
countries_gdf = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Filter countries within Europe
european_countries = countries_gdf[countries_gdf['CONTINENT'] == 'Europe']

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Filter points within Europe
europe_points = geo_df[geo_df['IsInEurope']]

# Create a plot
fig, ax = plt.subplots(figsize=(10, 10))

# Plot Europe shapefile
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot European countries
european_countries.plot(ax=ax, edgecolor='black', facecolor='none')

# Plot grassland locations
grassland_points = europe_points[europe_points['LC'] == 'C31']
grassland_points.plot(ax=ax, marker='.', color='green', label='Grassland')

# Plot cropland locations
cropland_points = europe_points[europe_points['LC'] == 'C11']
cropland_points.plot(ax=ax, marker='.', color='brown', label='Cropland')

# Add legend
ax.legend()

# Save the plot
plt.savefig('plots/plot27.png')
