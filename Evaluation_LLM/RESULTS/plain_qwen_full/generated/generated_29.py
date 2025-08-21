
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter the points where the carbon to nitrogen ratio is greater than 10
filtered_geo_df = geo_df[geo_df['CaCO3'] / geo_df['N'] > 10]

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')

# Plot the countries shapefile
countries_df.plot(ax=ax, color='white', edgecolor='black')

# Plot the filtered points
filtered_geo_df.plot(ax=ax, marker='.', color='red', markersize=5)

# Save the plot
plt.savefig('plots/plot29.png')
plt.close(fig)
