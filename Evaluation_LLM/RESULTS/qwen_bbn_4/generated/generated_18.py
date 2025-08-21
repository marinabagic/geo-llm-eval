
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load LUCAS data
df = pd.read_csv("LUCAS_with_country_info.csv")
df = df[df["LC0_Desc"] == "Woodland"]

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.TH_LONG, df.TH_LAT), crs="EPSG:4326")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")

# Load countries shapefile
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")

# Filter countries within Europe
countries_in_europe = world[world["CONTINENT"] == "Europe"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")
countries_in_europe.plot(ax=ax, color="none", edgecolor="black")
gdf.plot(ax=ax, color="green", markersize=5, marker='.')

plt.title("Woodland Areas in Europe")
plt.tight_layout()
plt.savefig('plots/plot18.png')
