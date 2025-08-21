
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Plot Europe
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot GeoDataFrame with land cover categories
geo_df.plot(ax=ax, column="LC1_Desc", legend=True, markersize=5, cmap="tab20")

# Set title and save plot
plt.title("Sampling Locations Colored by Detailed Land Cover Category")
plt.savefig('plots/plot23.png')
