
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter Austria from countries_df
austria_df = countries_df[countries_df["NAME"] == "Austria"]

# Filter geo_df for Austria, pH_CaCl2 > 5, and LC0_Desc is 'Woodland'
filtered_df = geo_df[(geo_df["NUTS_0"] == "AT") & (geo_df["pH_CaCl2"] > 5) & (geo_df["LC0_Desc"] == "Woodland")]

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot Europe
europe_df.plot(ax=ax, color="lightgrey")

# Plot Austria
austria_df.plot(ax=ax, color="white", edgecolor="black")

# Plot filtered points
filtered_df.plot(ax=ax, color="red", markersize=5, marker=".")

# Set limits to Austria's bounds
ax.set_xlim(austria_df.total_bounds[0], austria_df.total_bounds[2])
ax.set_ylim(austria_df.total_bounds[1], austria_df.total_bounds[3])

# Save plot
plt.savefig('plots/plot32.png', bbox_inches="tight", dpi=300)
plt.close()
