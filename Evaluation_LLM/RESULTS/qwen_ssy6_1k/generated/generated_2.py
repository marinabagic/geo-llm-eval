
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv('LUCAS.csv')
df['OC (20-30 cm)'] = pd.to_numeric(df['OC (20-30 cm)'], errors='coerce')
df = df.dropna(subset=['OC (20-30 cm)', 'LC0_Desc'])

avg_oc_by_lc = df.groupby('LC0_Desc')['OC (20-30 cm)'].mean().reset_index()

gdf = gpd.GeoDataFrame(avg_oc_by_lc, geometry=gpd.points_from_xy(avg_oc_by_lc.Latitude, avg_oc_by_lc.Longitude), crs="EPSG:4326")

europe = gpd.read_file("europe.gpkg")
europe["country"] = europe.apply(lambda row: row["NAME"].upper() if row["NAME"].upper() in df["NUTS_0"].unique() else None, axis=1)
europe = europe.dropna(subset=["country"])

fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

gdf.plot(ax=ax, column="OC (20-30 cm)", cmap="viridis", legend=True, markersize=10)

ax.set_title("Average Organic Carbon Content (0-20 cm) by General Land Cover Type")
plt.tight_layout()
plt.savefig('plots/plot2.png')
