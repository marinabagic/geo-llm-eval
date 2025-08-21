
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

top_10_percentile = gpd.read_file('geo_df.gpkg')['K'].quantile(0.90)
top_k_points = gpd.read_file('geo_df.gpkg')[gpd.read_file('geo_df.gpkg')['K'] > top_10_percentile]
europe_shapefile = gpd.read_file('europe.gpkg')
fig, ax = plt.subplots(figsize=(10, 10))
europe_shapefile.plot(ax=ax, color='lightgrey', edgecolor='black')
top_k_points.plot(ax=ax, marker='.', markersize=5, color='red')
plt.savefig('plots/top_10_percentile_k.png')
