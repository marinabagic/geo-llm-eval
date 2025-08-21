
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("LUCAS_with_country_info.csv")
df = df.dropna(subset=["TH_LAT", "TH_LONG"])

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")

# Load countries shapefile
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")
europe_countries = world[world["CONTINENT"] == "Europe"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf.plot(ax=ax, color="red", markersize=1, label="Soil Samples")

# Zoom to bounds of points
ax.set_xlim(gdf.total_bounds[0] - 1, gdf.total_bounds[2] + 1)
ax.set_ylim(gdf.total_bounds[1] - 1, gdf.total_bounds[3] + 1)

plt.title("All Soil Sample Points on Europe Map")
plt.legend()
plt.tight_layout()
plt.savefig('plots/plot16.png')
plt.show()
