
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("LUCAS_with_country_info.csv")
df["OC"] = pd.to_numeric(df["OC"], errors="coerce")

# Filter for Grassland or Woodland with OC > 20
df_filtered = df[(df["LC0_Desc"].isin(["Grassland", "Woodland"])) & (df["OC"] > 20)]

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df_filtered, geometry=gpd.points_from_xy(df_filtered["TH_LONG"], df_filtered["TH_LAT"]), crs="EPSG:4326")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")

# Load countries shapefile
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")
world.plot(ax=ax, color="white", edgecolor="black")
gdf.plot(ax=ax, marker='.', color="red", markersize=5)

plt.title("Points with OC > 20 in Grassland or Woodland")
plt.tight_layout()
plt.savefig('plots/plot20.png')
