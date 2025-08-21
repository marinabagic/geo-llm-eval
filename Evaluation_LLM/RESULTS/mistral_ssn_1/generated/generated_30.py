
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

geo_df_path = 'geo_df.gpkg'
geo_df = gpd.read_file(geo_df_path)
europe_shapefile_path = 'europe.gpkg'
europe_shapefile = gpd.read_file(europe_shapefile_path)

# Extract latitude and longitude columns
geo_df['lat'] = geo_df['TH_LAT']
geo_df['lon'] = geo_df['TH_LONG']

# Perform KMeans clustering on latitude and longitude
kmeans = KMeans(n_clusters=3)
geo_df['cluster'] = kmeans.fit_predict(geo_df[['lat', 'lon']])

fig, ax = plt.subplots(figsize=(10, 10))
europe_shapefile.plot(ax=ax, color='lightgrey')

# Plot clusters on the map
markers = ['o', 'x', '^']
colors = ['r', 'g', 'b']
for i in range(3):
    cluster_data = geo_df[geo_df['cluster'] == i]
    cluster_data.plot(ax=ax, marker=markers[i], color=colors[i], markersize=5)

plt.savefig('clusters.png')
