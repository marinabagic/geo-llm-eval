
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Filter points
filtered_df = geo_df[(geo_df["OC"] > 20) & (geo_df["LC"].isin(["Woodland", "Grassland"]))]

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
filtered_df.plot(ax=ax, marker=".", markersize=5, color="blue")

# Save plot
plt.savefig('plots/plot20.png', bbox_inches="tight", dpi=300)
plt.close()
