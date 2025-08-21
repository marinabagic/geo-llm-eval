
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("LUCAS_with_country_info.csv")
df["K"] = pd.to_numeric(df["K"], errors="coerce")

# Filter for Slovakia and K above 85th percentile
slovakia_k_85 = df[(df["Country"] == "Slovakia") & (df["K"] > df[df["Country"] == "Slovakia"]["K"].quantile(0.85))]
slovakia_k_85 = slovakia_k_85.dropna(subset=["TH_LONG", "TH_LAT"])

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(slovakia_k_85, geometry=gpd.points_from_xy(slovakia_k_85["TH_LONG"], slovakia_k_85["TH_LAT"]), crs="EPSG:4326")

# Load countries shapefile
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")
slovakia = world[world["NAME"] == "Slovakia"].explode(index_parts=True)

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
slovakia.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf.plot(ax=ax, marker='.', markersize=5)

ax.set_title("Slovakia: Points where 'K' is above 85th percentile")
plt.tight_layout()
plt.savefig('plots/plot34.png', dpi=300)
