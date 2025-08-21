
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load and filter data
df = pd.read_csv("LUCAS_with_country_info.csv")
df = df[df["Country"] == "Spain"]
df["OC"] = pd.to_numeric(df["OC"], errors="coerce")
df["K"] = pd.to_numeric(df["K"], errors="coerce")
df = df.dropna(subset=["OC", "K", "TH_LONG", "TH_LAT"])

# KMeans clustering
kmeans = KMeans(n_clusters=5, random_state=0)
df["Cluster"] = kmeans.fit_predict(df[["OC", "K"]])

# GeoDataFrame for points
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

# Load high-res world and get Spain
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")
spain = world[world["NAME"] == "Spain"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
spain.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf.plot(ax=ax, column="Cluster", cmap="tab10", markersize=5, legend=True, marker='.')

# Zoom to Spain’s polygon bounds
ax.set_xlim(*spain.total_bounds[[0, 2]])
ax.set_ylim(*spain.total_bounds[[1, 3]])

plt.title("KMeans Clustering on OC and K in Spain")
plt.tight_layout()
plt.savefig('plots/plot39.png')
