
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter Woodland areas with pH in water < 6
filtered_df = geo_df[(geo_df["LC0_Desc"] == "Woodland") & (geo_df["pH_H2O"] < 6)]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color="lightgrey")
countries_df.plot(ax=ax, color="white", edgecolor="black")
filtered_df.plot(ax=ax, color="green", markersize=5, label="Woodland (pH_H2O < 6)")

# Set limits to Europe
ax.set_xlim(europe_df.total_bounds[0], europe_df.total_bounds[2])
ax.set_ylim(europe_df.total_bounds[1], europe_df.total_bounds[3])

# Legend and title
ax.legend()
ax.set_title("Woodland Areas with pH in Water < 6 in Europe")

# Save plot
plt.savefig('plots/plot19.png')
plt.close()
