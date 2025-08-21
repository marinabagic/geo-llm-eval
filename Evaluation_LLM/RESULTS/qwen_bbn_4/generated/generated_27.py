
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load LUCAS data
df = pd.read_csv("LUCAS_with_country_info.csv")

# Filter for grassland and cropland
grassland_df = df[df["LC0_Desc"] == "Grassland"]
cropland_df = df[df["LC0_Desc"] == "Cropland"]

# Create GeoDataFrames
grassland_gdf = gpd.GeoDataFrame(grassland_df, geometry=gpd.points_from_xy(grassland_df["TH_LONG"], grassland_df["TH_LAT"]), crs="EPSG:4326")
cropland_gdf = gpd.GeoDataFrame(cropland_df, geometry=gpd.points_from_xy(cropland_df["TH_LONG"], cropland_df["TH_LAT"]), crs="EPSG:4326")

# Load Europe shapefile
europe_gdf = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")

# Load countries shapefile
world_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")
european_countries_gdf = world_gdf[world_gdf["CONTINENT"] == "Europe"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color="lightgrey")
european_countries_gdf.plot(ax=ax, color="none", edgecolor="black")
grassland_gdf.plot(ax=ax, color="green", marker='.', label="Grassland")
cropland_gdf.plot(ax=ax, color="yellow", marker='.', label="Cropland")

plt.title("Grassland vs Cropland Locations in Europe")
plt.legend()
plt.tight_layout()
plt.savefig('plots/plot27.png')
