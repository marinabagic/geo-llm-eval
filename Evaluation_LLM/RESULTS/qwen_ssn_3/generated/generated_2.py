
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')

# Calculate average organic carbon content (0-20 cm) by general land cover type
average_oc = geo_df.groupby('LC')['OC'].mean().reset_index()

# Plot the points with markers
geo_df.plot(ax=ax, x='TH_LONG', y='TH_LAT', marker='.', color='blue', markersize=5, legend=False)

# Add labels and title
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Average Organic Carbon Content (0-20 cm) by General Land Cover Type')

# Save the plot
plt.savefig('plots/plot2.png')
