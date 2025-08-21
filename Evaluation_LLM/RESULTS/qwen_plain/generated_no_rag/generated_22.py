
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Filter the points with electrical conductivity larger than 50
filtered_geo_df = geo_df[geo_df['EC'] > 50]

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')

# Plot the filtered points
filtered_geo_df.plot(ax=ax, marker='.', markersize=5, color='red')

# Save the plot
plt.savefig('plots/plot22.png')
plt.close(fig)
