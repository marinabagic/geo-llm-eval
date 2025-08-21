
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Load the Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot the GeoDataFrame
geo_df.plot(ax=ax, marker=".", column="CaCO3", legend=True)

# Save the plot
plt.savefig('plots/plot13.png')
