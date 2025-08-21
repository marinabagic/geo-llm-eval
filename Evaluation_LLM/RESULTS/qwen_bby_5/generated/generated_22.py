
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv("LUCAS_with_country_info.csv")
df["EC"] = pd.to_numeric(df["EC"], errors="coerce")
df = df[df["EC"].notna() & (df["EC"] > 50)]
df = df.dropna(subset=["TH_LAT", "TH_LONG"])

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")

fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf.plot(ax=ax, color="blue", markersize=5, marker=".")

plt.title("Electrical Conductivity > 50 in Europe")
plt.tight_layout()
plt.savefig('plots/plot22.png', dpi=300)
