
import geopandas as gpd
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Perform KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0)
geo_df['Cluster'] = kmeans.fit_predict(geo_df[['TH_LAT', 'TH_LONG']])

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color='lightgrey')

# Plot clustered points
for cluster_id in geo_df['Cluster'].unique():
    subset = geo_df[geo_df['Cluster'] == cluster_id]
    subset.plot(ax=ax, marker='.', color=plt.cm.tab10(cluster_id), label=f'Cluster {cluster_id + 1}')

ax.set_title('Europe with 3 Clusters of Coordinates')
ax.legend()
plt.tight_layout()

# Save the plot
plt.savefig('plots/plot30.png')
plt.close()
