import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Ensure plots directory exists
os.makedirs("plots", exist_ok=True)

# Load LUCAS data
df = pd.read_csv("LUCAS_with_country_info.csv")
df["OC"] = pd.to_numeric(df["OC"], errors="coerce")
df = df[(df["Country"] == "Croatia") & (df["OC"] < 20)]

# GeoDataFrame for points
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.TH_LONG, df.TH_LAT), crs="EPSG:4326")

# Load country shapefile and isolate Croatia
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")
croatia = countries[countries["NAME"] == "Croatia"].to_crs("EPSG:4326")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
croatia.plot(ax=ax, color="white", edgecolor="black")
gdf.plot(ax=ax, color="blue", marker=".", markersize=10)

plt.title("Points in Croatia where 'OC' < 20")
plt.tight_layout()
plt.savefig("plots/plot1.png")
