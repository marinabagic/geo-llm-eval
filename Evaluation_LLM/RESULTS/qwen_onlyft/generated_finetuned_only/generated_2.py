
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Group by land cover type and calculate average OC (0-20 cm)
avg_oc = geo_df.groupby("LC")["OC"].mean().reset_index()

# Create a new GeoDataFrame for the average OC values
avg_oc_gdf = gpd.GeoDataFrame(avg_oc, geometry=gpd.points_from_xy(0, 0), crs="EPSG:4326")

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot average OC values
for idx, row in avg_oc_gdf.iterrows():
    ax.annotate(f"{row['LC']}: {row['OC']:.2f}", xy=(0, 0), xytext=(10, -10 * idx),
                textcoords="offset points", ha="left", va="bottom")

# Set title and save plot
ax.set_title("Average Organic Carbon Content (0-20 cm) by Land Cover Type")
plt.tight_layout()
plt.savefig('plots/plot2.png')
plt.close()
