
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Filter points where organic carbon content is available
available_oc_points = geo_df[geo_df['OC'].notna()]

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Load countries shapefile
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot Europe shapefile
europe.plot(ax=ax, color="lightgrey", edgecolor="black")

# Plot countries
countries.plot(ax=ax, color="none", edgecolor="black")

# Plot points with available organic carbon content
available_oc_points.plot(ax=ax, marker='.', color="red", markersize=5)

# Save the plot
plt.savefig('plots/plot26.png', bbox_inches="tight", dpi=300)
