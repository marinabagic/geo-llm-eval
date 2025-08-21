
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")

# Filter points with EC > 50
filtered_geo_df = geo_df[geo_df["EC"] > 50]

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color="lightgrey")

# Plot filtered points
filtered_geo_df.plot(ax=ax, marker=".", markersize=5, color="red", label="EC > 50")

# Set title and legend
ax.set_title("Points with Electrical Conductivity > 50 in Europe")
ax.legend()

# Save plot
plt.savefig('plots/plot22.png')
plt.close()
