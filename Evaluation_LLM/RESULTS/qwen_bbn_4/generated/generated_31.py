
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("LUCAS_with_country_info.csv")
df["OC"] = pd.to_numeric(df["OC"], errors="coerce")

# Filter for Croatia and OC below 20
df = df[(df["Country"] == "Croatia") & (df["OC"] < 20)]
df = df.dropna(subset=["TH_LONG", "TH_LAT"])

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

# Load the countries shapefile
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")

# Filter for Croatia
croatia = world[world["NAME"] == "Croatia"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
croatia.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf.plot(ax=ax, marker='.', color="red", markersize=5)

ax.set_title("Points in Croatia where OC is below 20")
plt.tight_layout()
plt.savefig('plots/plot31.png', dpi=300)
