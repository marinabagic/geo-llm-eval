
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load and filter LUCAS data
df = pd.read_csv("LUCAS_with_country_info.csv")
df["pH_CaCl2"] = pd.to_numeric(df["pH_CaCl2"], errors="coerce")
df = df[(df["Country"] == "Austria") & (df["pH_CaCl2"] > 5) & (df["LC0_Desc"] == "Woodland")]

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.TH_LONG, df.TH_LAT), crs="EPSG:4326")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")

# Load countries shapefile
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")
austria = world[world["NAME"] == "Austria"].explode(index_parts=True)
austria["area"] = austria.geometry.area
austria_main = austria[austria["area"] > 1]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
austria_main.plot(ax=ax, color="white", edgecolor="black")
if not gdf.empty:
    gdf.plot(ax=ax, color="blue", markersize=5, marker='.')
    ax.set_title("pH_CaCl2 > 5 in Austrian Woodland")
else:
    ax.set_title("No matching data for Austria (pH_CaCl2 > 5 & Woodland)")
ax.set_xlim(austria_main.total_bounds[0] - 0.5, austria_main.total_bounds[2] + 0.5)
ax.set_ylim(austria_main.total_bounds[1] - 0.5, austria_main.total_bounds[3] + 0.5)
plt.tight_layout()
plt.savefig('plots/plot32.png', dpi=300)
