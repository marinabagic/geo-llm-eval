
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter Slovakia from countries_df
slovakia = countries_df[countries_df["NAME"] == "Slovakia"]

# Calculate 85th percentile of 'K' for Slovakia
k_threshold = geo_df[geo_df["NUTS_0"] == "SK"]["K"].quantile(0.85)

# Filter points in Slovakia where 'K' is above the threshold
slovakia_points = geo_df[(geo_df["NUTS_0"] == "SK") & (geo_df["K"] > k_threshold)]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))

# Plot Europe
europe_df.plot(ax=ax, color="lightgrey")

# Plot Slovakia
slovakia.plot(ax=ax, color="white", edgecolor="black")

# Plot points
slovakia_points.plot(ax=ax, color="red", markersize=5, marker=".")

# Set limits
ax.set_xlim(slovakia.total_bounds[0] - 0.5, slovakia.total_bounds[2] + 0.5)
ax.set_ylim(slovakia.total_bounds[1] - 0.5, slovakia.total_bounds[3] + 0.5)

# Save plot
plt.savefig('plots/plot34.png', bbox_inches="tight", dpi=300)
plt.close()
