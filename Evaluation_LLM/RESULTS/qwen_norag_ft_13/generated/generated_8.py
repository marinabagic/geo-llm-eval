
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = gpd.read_file("geo_df.gpkg")
europe = gpd.read_file("europe.gpkg")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter European countries
europe_countries = countries[countries["CONTINENT"] == "Europe"]

# Plot Europe
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot European countries
europe_countries.plot(ax=ax, edgecolor="black", facecolor="none")

# Plot points
df.plot(ax=ax, column="EC", cmap="viridis", markersize=5, legend=True)

# Set limits
ax.set_xlim(europe.total_bounds[0] - 1, europe.total_bounds[2] + 1)
ax.set_ylim(europe.total_bounds[1] - 1, europe.total_bounds[3] + 1)

# Save plot
plt.savefig('plots/plot8.png')
plt.close()

# Boxplot of EC grouped by land use class
df.boxplot(column="EC", by="LU1_Desc", figsize=(15, 10))

# Save boxplot
plt.savefig('plots/plot8.png')
plt.close()
