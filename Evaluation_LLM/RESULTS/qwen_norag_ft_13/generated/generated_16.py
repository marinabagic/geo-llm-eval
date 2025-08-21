
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter countries to only include those in Europe
europe_countries = countries_df[countries_df['CONTINENT'] == 'Europe']

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')

# Plot filtered European countries
europe_countries.plot(ax=ax, edgecolor='black', facecolor='none')

# Plot soil sample points
geo_df.plot(ax=ax, marker='.', color='blue', markersize=1)

# Set limits to Europe only
ax.set_xlim(europe_df.total_bounds[0], europe_df.total_bounds[2])
ax.set_ylim(europe_df.total_bounds[1], europe_df.total_bounds[3])

# Save plot
plt.savefig('plots/plot16.png', dpi=300)
plt.close()
