
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')

# Plot countries within Europe
countries_in_europe = countries_df[countries_df['ISO_A2'].isin(europe_df['NUTS_0'])]
countries_in_europe.plot(ax=ax)

# Plot points from geo_df
geo_df.plot(ax=ax, marker='.', markersize=1, color='black')

# Save the plot
plt.savefig('plots/plot8.png')
plt.close(fig)
