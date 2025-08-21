
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Filter for nitrogen outliers (N > 4)
outliers = geo_df[geo_df["N"] > 4]

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
outliers.plot(ax=ax, marker=".", markersize=5, color="red")

# Save plot
plt.savefig('plots/plot25.png', bbox_inches="tight", dpi=300)
plt.close()
