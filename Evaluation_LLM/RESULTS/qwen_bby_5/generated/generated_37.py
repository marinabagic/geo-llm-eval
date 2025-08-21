
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load and filter data
df = pd.read_csv("LUCAS_with_country_info.csv")
df = df[df["Country"] == "France"]

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

# Load high-resolution country borders and extract France
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")
france_shape = world[world["NAME"] == "France"].to_crs("EPSG:4326")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
france_shape.plot(ax=ax, color="white", edgecolor="black")
gdf.plot(ax=ax, column="LC0_Desc", cmap="tab10", markersize=5, legend=True)
ax.set_title("Land Cover Categories in France")
plt.tight_layout()
plt.savefig('plots/plot37.png')
plt.show()
