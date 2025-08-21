
import geopandas as gpd
import matplotlib.pyplot as plt

geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

top_10_percentile = geo_df['K'].quantile(0.90)
top_k_points = geo_df[geo_df['K'] > top_10_percentile]

fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey', edgecolor='black')
top_k_points.plot(ax=ax, marker='.', color='red', markersize=5)

plt.title('Top 10% of Potassium Values in Europe')
plt.savefig('plots/plot21.png')
