
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Filter for Woodland areas
woodland_df = geo_df[geo_df["LC0_Desc"] == "Woodland"]

# Load the Europe shapefile
europe_df = gpd.read_file("europe.gpkg")

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color="lightgrey", edgecolor="black")

# Plot Woodland areas
woodland_df.plot(ax=ax, marker=".", color="green", markersize=5, label="Woodland")

# Set title and legend
ax.set_title("Woodland Areas in Europe")
ax.legend()

# Save the plot
plt.savefig('plots/plot18.png')
plt.close()
