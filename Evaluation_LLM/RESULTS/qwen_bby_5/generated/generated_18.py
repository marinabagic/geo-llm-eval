
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("LUCAS_with_country_info.csv")
df = df[df["LC0_Desc"] == "Woodland"]

# GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.TH_LONG, df.TH_LAT), crs="EPSG:4326")

# Load high-res shapefile and filter to Europe only
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")
europe = world[world["CONTINENT"] == "Europe"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf[gdf["Country"].isin(europe["NAME"])].plot(ax=ax, color="green", markersize=5, label="Woodland")

plt.title("Woodland Areas in Europe")
plt.legend()
plt.tight_layout()
plt.savefig('plots/plot18.png')
