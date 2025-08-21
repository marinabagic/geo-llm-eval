
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv("LUCAS_with_country_info.csv")
df = df[df["Country"] == "Poland"]
df["OC"] = pd.to_numeric(df["OC"], errors="coerce")
df = df.dropna(subset=["OC", "TH_LONG", "TH_LAT"])
median_oc = df["OC"].median()
df = df[df["OC"] > median_oc]

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")
poland = world[world["NAME"] == "Poland"]

fig, ax = plt.subplots(figsize=(10, 10))
poland.plot(ax=ax, color="white", edgecolor="black")
gdf.plot(ax=ax, column="LU_DESC", cmap="tab10", markersize=10, legend=True)
ax.set_title("OC > Median in Poland (colored by LU_DESC)")
plt.tight_layout()
plt.savefig('plots/plot36.png')
plt.show()
