
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter for Belgium
belgium = countries_df[countries_df["NAME"] == "Belgium"]

# Filter points in Belgium
points_in_belgium = geo_df[geo_df["NUTS_0"] == "BE"]

# Calculate bottom 10th percentile of pH_H2O
pH_H2O_threshold = points_in_belgium["pH_H2O"].quantile(0.1)

# Filter points with pH_H2O below threshold
filtered_points = points_in_belgium[points_in_belgium["pH_H2O"] <= pH_H2O_threshold]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color="lightgrey")
belgium.plot(ax=ax, color="white", edgecolor="black")
filtered_points.plot(ax=ax, color="red", markersize=5, label="pH_H2O < 10th percentile")

ax.set_title("Belgium - Points with Low pH_H2O")
ax.legend()

plt.savefig('plots/plot35.png')
plt.close()
