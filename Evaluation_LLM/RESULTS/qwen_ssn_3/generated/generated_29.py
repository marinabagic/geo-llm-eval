
import geopandas as gpd
import matplotlib.pyplot as plt

# Read the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Calculate the carbon to nitrogen ratio
geo_df['C_N_ratio'] = geo_df['CaCO3'] / geo_df['N']

# Filter points where the carbon to nitrogen ratio is greater than 10
filtered_points = geo_df[geo_df['C_N_ratio'] > 10]

# Plot the Europe shapefile and the filtered points
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')
filtered_points.plot(ax=ax, marker='.', color='red')

# Save the plot
plt.savefig('plots/plot29.png')
