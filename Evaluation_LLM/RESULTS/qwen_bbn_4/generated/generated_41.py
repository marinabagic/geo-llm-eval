
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("LUCAS_with_country_info.csv")
df = df[df["Country"] == "Italy"]

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

# Load high-res Italy shape
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")
italy = world[world["NAME"] == "Italy"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
italy.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf.plot(ax=ax, column="LC0_Desc", cmap="tab10", markersize=5, legend=True, marker='.')

ax.set_title("Italy Soil Points Colored by LC0_Desc")
plt.tight_layout()
plt.savefig('plots/plot41.png')
