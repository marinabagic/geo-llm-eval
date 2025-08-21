
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# Load GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color="lightgrey")

# Plot GeoDataFrame
geo_df.plot(ax=ax, marker=".", column="NUTS_0", legend=True)

# Save plot
plt.savefig('plots/plot8.png')
plt.close()

# Boxplot of EC grouped by land use class
plt.figure(figsize=(10, 10))
geo_df.boxplot(column="EC", by="LU", grid=False)
plt.suptitle("")  # Remove main title
plt.title("EC by Land Use Class")
plt.xlabel("Land Use Class")
plt.ylabel("EC")
plt.xticks(rotation=45)
plt.tight_layout()

# Save plot
plt.savefig('plots/plot8.png')
plt.close()
