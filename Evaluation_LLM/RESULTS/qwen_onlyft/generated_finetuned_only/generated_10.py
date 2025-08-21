
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color="lightgrey")

# Plot GeoDataFrame points
geo_df.plot(ax=ax, column="pH_H2O", cmap="viridis", marker=".", legend=True)

# Set title and save plot
ax.set_title("pH in Water vs Potassium with Europe Border")
plt.savefig('plots/plot10.png')
plt.close()
