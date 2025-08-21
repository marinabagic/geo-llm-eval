
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe = gpd.read_file("europe.gpkg")

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot GeoDataFrame
geo_df.plot(ax=ax, marker=".", markersize=1, color="blue")

# Save plot
plt.savefig('plots/plot15.png', bbox_inches="tight")
plt.close()
