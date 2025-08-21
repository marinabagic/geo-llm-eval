
import geopandas as gpd
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter countries within Europe
europe_countries = countries_df[countries_df['CONTINENT'] == 'Europe']

# Perform KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
geo_df['Cluster'] = kmeans.fit_predict(geo_df[['TH_LAT', 'TH_LONG']])

# Plot
fig, ax = plt.subplots(figsize=(10, 10))

europe_df.plot(ax=ax, color='lightgrey')
europe_countries.plot(ax=ax, color='white', edgecolor='black')

for cluster_id in geo_df['Cluster'].unique():
    subset = geo_df[geo_df['Cluster'] == cluster_id]
    subset.plot(ax=ax, marker='.', color=plt.cm.tab10(cluster_id), label=f'Cluster {cluster_id + 1}')

ax.set_title('Europe with 3 Clusters of Coordinates')
ax.legend()
ax.set_xlim(europe_df.total_bounds[0] - 1, europe_df.total_bounds[2] + 1)
ax.set_ylim(europe_df.total_bounds[1] - 1, europe_df.total_bounds[3] + 1)

plt.savefig('plots/plot30.png')
plt.close()
