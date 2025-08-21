
import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file('geo_df.gpkg')
europe_shapefile = gpd.read_file('europe.gpkg')

fig, ax = plt.subplots(figsize=(10, 10))
europe_shapefile.plot(ax=ax, color='lightgrey', edgecolor='black')
gdf.plot(ax=ax, marker='.', color='blue', markersize=5)
plt.title('Soil Sample Points on Europe Map')
plt.savefig('plots/plot16.png')
