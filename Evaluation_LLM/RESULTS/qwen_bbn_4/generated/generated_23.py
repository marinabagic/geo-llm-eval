
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load LUCAS data
df = pd.read_csv("LUCAS_with_country_info.csv")

# Filter for Europe
df = df[df["IsInEurope"] == True]

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
europe_countries.plot(ax=ax, color="none", edgecolor="black")
gdf.plot(ax=ax, column="LC0_Desc", cmap="tab10", markersize=5, legend=True, marker='.')

ax.set_title("Sampling Locations Colored by Detailed Land Cover Category in Europe")
plt.tight_layout()
plt.savefig('plots/plot23.png')
