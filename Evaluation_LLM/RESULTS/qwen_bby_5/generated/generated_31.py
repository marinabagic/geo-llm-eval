
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv("LUCAS_with_country_info.csv")
df["OC"] = pd.to_numeric(df["OC"], errors="coerce")
df = df.dropna(subset=["OC", "TH_LONG", "TH_LAT"])
df = df[(df["Country"] == "Croatia") & (df["OC"] < 20)]

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")
croatia = europe[europe["NAME"] == "Croatia"].explode(index_parts=True)

fig, ax = plt.subplots(figsize=(10, 10))
croatia.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf.plot(ax=ax, color="red", marker=".", markersize=5)

ax.set_title("Croatia: OC Below 20")
plt.tight_layout()
plt.savefig('plots/plot31.png', dpi=300)
