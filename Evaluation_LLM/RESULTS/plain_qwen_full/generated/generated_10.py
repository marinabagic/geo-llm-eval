
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter countries within Europe
europe_countries = countries_df[countries_df['CONTINENT'] == 'Europe']

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')

# Plot countries within Europe
europe_countries.plot(ax=ax, edgecolor='black', facecolor='none')

# Plot points from geo_df
geo_df.plot(ax=ax, x='TH_LONG', y='TH_LAT', marker='.', color='red')

# Save the plot
plt.savefig('plots/plot10.png')
plt.close(fig)
