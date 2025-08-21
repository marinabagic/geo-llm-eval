
import geopandas as gpd
import matplotlib.pyplot as plt

# Read the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the Europe shapefile with lightgrey color
europe_df.plot(ax=ax, color='lightgrey', edgecolor='black')

# Plot the pH_H2O values from geo_df
geo_df.plot(ax=ax, column='pH_H2O', legend=True, marker='.', markersize=5, cmap='viridis')

# Save the plot
plt.savefig('plots/plot24.png')
