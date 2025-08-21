
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv("LUCAS_with_country_info.csv")
df = df[df["IsInEurope"] == True]
df["LC0_Desc"] = df["LC0_Desc"].replace({"Other herbaceous vegetation": "Grassland"})
df = df[df["LC0_Desc"].isin(["Grassland", "Cropland"])]
df = df.dropna(subset=["TH_LAT", "TH_LONG"])

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")

fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf[gdf["LC0_Desc"] == "Grassland"].plot(ax=ax, color="green", markersize=5, label="Grassland")
gdf[gdf["LC0_Desc"] == "Cropland"].plot(ax=ax, color="orange", markersize=5, label="Cropland")

plt.title("Grassland vs Cropland Locations in Europe")
plt.legend()
plt.tight_layout()
plt.savefig('plots/plot27.png')
plt.show()
