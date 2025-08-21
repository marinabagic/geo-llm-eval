
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv("LUCAS_with_country_info.csv")
df = df[df["Country"] == "Germany"]
df["pH_H2O"] = pd.to_numeric(df["pH_H2O"], errors="coerce")
df = df.dropna(subset=["pH_H2O", "NUTS_2"])

avg_ph_h2o = df.groupby("NUTS_2")["pH_H2O"].mean().reset_index()

gdf = gpd.GeoDataFrame(avg_ph_h2o, geometry=None, crs="EPSG:4326")

germany = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")
germany = germany[germany["NAME"] == "Germany"].explode(index_parts=True)

fig, ax = plt.subplots(figsize=(10, 10))
germany.plot(ax=ax, color="lightgrey", edgecolor="black")

gdf = gdf.merge(germany, left_on="NUTS_2", right_on="STAT_LEVL_2")
gdf.plot(ax=ax, column="pH_H2O", legend=True, cmap="viridis", markersize=0)

ax.set_title("Average pH_H2O per NUTS2 Region in Germany")
ax.set_xlim(germany.total_bounds[0] - 0.2, germany.total_bounds[2] + 0.2)
ax.set_ylim(germany.total_bounds[1] - 0.2, germany.total_bounds[3] + 0.2)

plt.tight_layout()
plt.savefig('plots/plot40.png')
plt.close()
