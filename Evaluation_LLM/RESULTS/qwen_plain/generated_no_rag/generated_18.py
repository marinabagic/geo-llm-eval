
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Filter the GeoDataFrame to include only Woodland areas
woodland_df = geo_df[geo_df['LC'] == 'Woodland']

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')

# Plot the Woodland areas
woodland_df.plot(ax=ax, marker='.', markersize=1, color='blue')

# Save the plot
plt.savefig('plots/plot18.png')
