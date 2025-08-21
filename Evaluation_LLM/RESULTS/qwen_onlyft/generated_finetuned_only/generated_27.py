
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrame and Europe shapefile
geo_df = gpd.read_file("geo_df.gpkg")
europe = gpd.read_file("europe.gpkg")

# Filter GeoDataFrame for grassland and cropland
grassland = geo_df[geo_df["LC"] == "C31"]
cropland = geo_df[geo_df["LC"] == "C12"]

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot grassland and cropland
grassland.plot(ax=ax, color="green", marker=".", label="Grassland")
cropland.plot(ax=ax, color="brown", marker=".", label="Cropland")

# Add legend and title
ax.legend()
ax.set_title("Grassland vs Cropland Locations on Europe Map")

# Save plot
plt.savefig('plots/plot27.png')
plt.close()
