
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_gdf = gpd.read_file("europe.gpkg")

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot the points from geo_df
geo_df.plot(ax=ax, marker='.', markersize=1, color='blue')

# Save the plot
plt.savefig('plots/plot1.png')

# Find the general land cover class with the highest average soil pH in water
average_pH = geo_df.groupby('LC0_Desc')['pH_H2O'].mean()
result = average_pH.idxmax()

print(result)
