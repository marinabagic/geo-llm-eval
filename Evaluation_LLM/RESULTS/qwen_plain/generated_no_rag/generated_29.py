
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')

# Calculate the carbon to nitrogen ratio
geo_df['C_N_Ratio'] = geo_df['CaCO3'] / geo_df['N']

# Filter points where the carbon to nitrogen ratio is greater than 10
filtered_points = geo_df[geo_df['C_N_Ratio'] > 10]

# Plot the Europe shapefile
ax = europe_gdf.plot(color='lightgrey', figsize=(10, 10))

# Plot the filtered points
filtered_points.plot(ax=ax, marker='.', markersize=5)

# Save the plot
plt.savefig('plots/plot29.png')
