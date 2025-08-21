
import geopandas as gpd
import matplotlib.pyplot as plt

geo_df = gpd.read_file('geo_df.gpkg')
c_n_threshold = 10

fig, ax = plt.subplots(figsize=(10, 10))
europe_df = gpd.read_file('europe.gpkg')
europe_df.plot(ax=ax, color='lightgrey')

high_c_n_points = geo_df[geo_df['C/N'] > c_n_threshold]
high_c_n_points.plot(ax=ax, marker='.', markersize=5, color='red')

plt.savefig('plots/high_c_n_points.png')
