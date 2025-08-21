
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe = gpd.read_file("europe.gpkg")

# Filter points with pH_CaCl2 > 6
filtered_geo_df = geo_df[geo_df["pH_CaCl2"] > 6]

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot filtered points
filtered_geo_df.plot(ax=ax, marker=".", markersize=5, color="red")

# Set extent to Europe
ax.set_xlim(europe.total_bounds[0], europe.total_bounds[2])
ax.set_ylim(europe.total_bounds[1], europe.total_bounds[3])

# Save plot
plt.savefig('plots/plot17.png', bbox_inches="tight", dpi=300)
plt.close()
