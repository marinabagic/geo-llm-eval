
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv("LUCAS_with_country_info.csv")
df["TH_LAT"] = pd.to_numeric(df["TH_LAT"], errors="coerce")
df["TH_LONG"] = pd.to_numeric(df["TH_LONG"], errors="coerce")
df = df.dropna(subset=["TH_LAT", "TH_LONG", "LC0_Desc"])

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")
london = gpd.GeoSeries([Point(-0.1278, 51.5074)], crs="EPSG:4326")
buffer = london.buffer(100000).iloc[0]

gdf_filtered = gdf[gdf.geometry.within(buffer)]

europe = gpd.read_file("europe.gpkg").to_crs(epsg=3035)
europe.plot(ax=ax, color="lightgrey")

fig, ax = plt.subplots(figsize=(10, 10))
gdf_filtered.plot(ax=ax, column="LC0_Desc", cmap="tab10", markersize=10, legend=True)
ax.set_title("Points within 100 km of London, colored by LC0_Desc")
plt.tight_layout()
plt.savefig('plots/plot38.png')
plt.show()
