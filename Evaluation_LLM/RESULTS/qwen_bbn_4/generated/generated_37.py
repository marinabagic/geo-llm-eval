
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load LUCAS data and filter for France
df = pd.read_csv("LUCAS_with_country_info.csv")
df = df[df["Country"] == "France"]

# Fallback for LU_DESC
if "LU_DESC" not in df.columns and "LC0_Desc" in df.columns:
    df["LU_DESC"] = df["LC0_Desc"]

# Clean
df = df.dropna(subset=["LU_DESC", "TH_LAT", "TH_LONG"])

# GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

# Load high-res shapefile and extract France
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")
france = world[world["NAME"] == "France"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
france.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf.plot(ax=ax, column="LU_DESC", cmap="tab10", markersize=5, legend=True, marker='.')

plt.title("Land Cover Categories in France")
plt.tight_layout()
plt.savefig('plots/plot37.png')
