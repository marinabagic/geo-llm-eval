
import geopandas as gpd
import matplotlib.pyplot as plt

geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

filtered_geo_df = geo_df[geo_df['EC'] > 50]

fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')
filtered_geo_df.plot(ax=ax, marker='.', color='red')

plt.savefig('plots/plot22.png')
