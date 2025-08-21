
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot soil sample points
geo_df.plot(ax=ax, marker=".", markersize=1, color="black")

# Set extent to Europe
ax.set_xlim(europe.total_bounds[0], europe.total_bounds[2])
ax.set_ylim(europe.total_bounds[1], europe.total_bounds[3])

# Save plot
plt.savefig('plots/plot16.png', dpi=300)
plt.close()
