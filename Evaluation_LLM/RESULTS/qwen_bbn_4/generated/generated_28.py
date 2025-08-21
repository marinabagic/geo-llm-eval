
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load LUCAS dataset
df = pd.read_csv("LUCAS_with_country_info.csv")

# Filter for spruce and pine dominated forests
spruce_forest = df[df["LC1_Desc"] == "Spruce dominated coniferous woodland"]
pine_forest = df[df["LC1_Desc"] == "Pine dominated coniferous woodland"]

# Create GeoDataFrames
gdf_spruce = gpd.GeoDataFrame(spruce_forest, geometry=gpd.points_from_xy(spruce_forest["TH_LONG"], spruce_forest["TH_LAT"]), crs="EPSG:4326")
gdf_pine = gpd.GeoDataFrame(pine_forest, geometry=gpd.points_from_xy(pine_forest["TH_LONG"], pine_forest["TH_LAT"]), crs="EPSG:4326")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")

# Load countries shapefile and filter for Europe
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")
europe_countries = world[world["CONTINENT"] == "Europe"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")
europe_countries.plot(ax=ax, color="none", edgecolor="black")
gdf_spruce.plot(ax=ax, color="green", markersize=5, marker='.', label="Spruce Dominated Forest")
gdf_pine.plot(ax=ax, color="red", markersize=5, marker='.', label="Pine Dominated Forest")

plt.title("Spruce vs Pine Dominated Forests in Europe")
plt.legend()
plt.tight_layout()
plt.savefig('plots/plot28.png')
