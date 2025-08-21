
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot GeoDataFrame
geo_df.plot(ax=ax, column="pH_H2O", marker=".", legend=True)

# Save plot
plt.savefig('plots/plot1.png')

# Find general land cover class with highest average soil pH in water
average_ph_h2o_by_lc = geo_df.groupby("LC")["pH_H2O"].mean().reset_index()
highest_avg_ph_h2o_class = average_ph_h2o_by_lc.loc[average_ph_h2o_by_lc["pH_H2O"].idxmax(), "LC"]

print(highest_avg_ph_h2o_class)
