
import geopandas as gpd
import pandas as pd

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot GeoDataFrame
geo_df.plot(ax=ax, marker=".", column="K", legend=True)

# Save plot
plt.savefig('plots/plot7.png')

# Top 3 regions (NUTS_2) with highest potassium
top_regions = geo_df.groupby("NUTS_2")["K"].mean().nlargest(3)
print(top_regions)
