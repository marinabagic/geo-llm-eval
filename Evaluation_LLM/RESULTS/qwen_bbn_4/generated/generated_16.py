
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrame from the specified file
geo_df = gpd.read_file("geo_df.gpkg")

# Load the Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Load the countries shapefile
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot Europe shapefile with lightgrey color
europe.plot(ax=ax, color="lightgrey", edgecolor="black")

# Plot countries shapefile
countries.plot(ax=ax, color="none", edgecolor="black")

# Plot the soil sample points
geo_df.plot(ax=ax, marker='.', color="red", markersize=5)

# Save the plot
plt.title("Soil Sample Points on Europe Map")
plt.tight_layout()
plt.savefig('plots/plot16.png')
