
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

# Filter for spruce and pine dominated forests
spruce_forests = geo_df[geo_df['LC1_Desc'] == 'Spruce dominated coniferous woodland']
pine_forests = geo_df[geo_df['LC1_Desc'] == 'Pine dominated coniferous woodland']

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot Europe
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot European countries
european_countries.plot(ax=ax, edgecolor='black', facecolor='none')

# Plot spruce forests
spruce_forests.plot(ax=ax, marker='.', color='green', markersize=5, label='Spruce Dominated Forests')

# Plot pine forests
pine_forests.plot(ax=ax, marker='.', color='red', markersize=5, label='Pine Dominated Forests')

# Add legend
ax.legend()

# Save the plot
plt.savefig('plots/plot28.png')
