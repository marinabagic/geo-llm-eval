
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load and filter data
df = pd.read_csv("LUCAS_with_country_info.csv")
df["EC"] = pd.to_numeric(df["EC"], errors="coerce")
df = df[df["EC"] > 50]
df = df.dropna(subset=["TH_LAT", "TH_LONG"])

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

# Load high-res countries shapefile and filter to Europe only
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")
europe = world[world["CONTINENT"] == "Europe"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf.plot(ax=ax, color="blue", markersize=5, marker='.', label="EC > 50")

# Set tight limits around Europe only
bbox = gdf.total_bounds
ax.set_xlim(bbox[0], bbox[2])
ax.set_ylim(bbox[1], bbox[3])

plt.title("Points with Electrical Conductivity > 50 in Europe")
plt.legend()
plt.tight_layout()
plt.savefig('plots/plot22.png', dpi=300)
