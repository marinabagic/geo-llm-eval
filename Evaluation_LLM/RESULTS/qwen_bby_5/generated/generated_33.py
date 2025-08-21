
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv("LUCAS_with_country_info.csv")
df["SURVEY_DATE"] = pd.to_datetime(df["SURVEY_DATE"], format="%d-%m-%y")
df = df[(df["SURVEY_DATE"].dt.month == 7) & (df["SURVEY_DATE"].dt.year == 2018)]

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")
europe.plot(ax=ax, color="lightgrey", edgecolor="black")

fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax, column="LC0_Desc", cmap="tab10", markersize=5, legend=True)
ax.set_title("July 2018 Samples by Land Cover Category")
plt.tight_layout()
plt.savefig('plots/plot33.png')
plt.show()
