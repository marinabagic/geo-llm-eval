
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("LUCAS_with_country_info.csv")
df = df.dropna(subset=["LC1_Desc", "TH_LAT", "TH_LONG"])

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

# Load European borders
world = gpd.read_file("europe.gpkg")
europe = world.to_crs("EPSG:4326")

# Get bounding box
bbox = gdf.total_bounds

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf.plot(ax=ax, column="LC1_Desc", cmap="tab20", markersize=5, legend=True)

ax.set_xlim(bbox[0], bbox[2])
ax.set_ylim(bbox[1], bbox[3])
ax.set_title("Sampling Locations Colored by Detailed Land Cover Category on Europe Map")
plt.tight_layout()
plt.savefig('plots/plot23.png')
