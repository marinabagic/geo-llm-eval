
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Perform KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0).fit(geo_df[['TH_LONG', 'TH_LAT']])
geo_df['Cluster'] = kmeans.labels_

fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')
geo_df.plot(ax=ax, column='Cluster', cmap='viridis', marker='.', legend=True)

plt.savefig('plots/plot30.png')
