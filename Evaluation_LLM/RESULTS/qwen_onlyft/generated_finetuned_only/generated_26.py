
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Filter rows where OC is not NaN
geo_df = geo_df[~geo_df["OC"].isna()]

# Load the Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot the filtered GeoDataFrame
geo_df.plot(ax=ax, column="OC", legend=True, marker=".", cmap="viridis")

# Save the plot
plt.savefig('plots/plot26.png')
plt.close()
