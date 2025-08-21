
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Filter for spruce and pine dominated forests
spruce_df = geo_df[geo_df["LC1_Desc"] == "Spruce dominated coniferous woodland"]
pine_df = geo_df[geo_df["LC1_Desc"] == "Pine dominated coniferous woodland"]

# Load Europe shapefile
europe_df = gpd.read_file("europe.gpkg")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color="lightgrey")
spruce_df.plot(ax=ax, color="green", markersize=5, label="Spruce Dominated")
pine_df.plot(ax=ax, color="red", markersize=5, label="Pine Dominated")

ax.legend()
plt.tight_layout()
plt.savefig('plots/plot28.png')
plt.close()
