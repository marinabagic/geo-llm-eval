
import geopandas as gpd
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter for Spain
spain_df = countries_df[countries_df["NAME"] == "Spain"]

# Perform KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0)
geo_df["Cluster"] = kmeans.fit_predict(geo_df[["OC", "K"]])

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color="lightgrey")
spain_df.plot(ax=ax, color="white", edgecolor="black")
geo_df.plot(ax=ax, column="Cluster", cmap="viridis", markersize=5, legend=True)

ax.set_title("KMeans Clustering on OC and K in Spain")
plt.savefig('plots/plot39.png')
plt.close()
