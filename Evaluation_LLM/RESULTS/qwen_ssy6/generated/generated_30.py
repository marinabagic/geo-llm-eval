
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

geo_df_path = 'geo_df.gpkg'
geo_df = gpd.read_file(geo_df_path)
europe_shapefile_path = 'europe.gpkg'
europe_shapefile = gpd.read_file(europe_shapefile_path)

kmeans = KMeans(n_clusters=3)
geo_df['cluster'] = kmeans.fit_predict(geo_df[['TH_LAT', 'TH_LONG']])

fig, ax = plt.subplots(figsize=(10, 10))
europe_shapefile.plot(ax=ax, color='lightgrey')
geo_df.plot(ax=ax, marker='.', column='cluster', cmap='viridis', legend=True)

plt.savefig('plots/plot30.png')
