
import pandas as pd
import geopandas as gpd
import scipy.stats as stats

df = pd.read_csv('LUCAS.csv')
df["EC_zscore"] = stats.zscore(df["EC"], nan_policy="omit")
outliers = df[(df["EC_zscore"] > 3) | (df["EC_zscore"] < -3)]

europe = gpd.read_file("europe.gpkg")
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

if not outliers.empty:
    gdf = gpd.GeoDataFrame(outliers, geometry=gpd.points_from_xy(outliers.TH_LONG, outliers.TH_LAT), crs="EPSG:4326")
    gdf.plot(ax=ax, column="EC", marker=".", legend=True)

plt.tight_layout()
plt.savefig('plots/plot11.png')
