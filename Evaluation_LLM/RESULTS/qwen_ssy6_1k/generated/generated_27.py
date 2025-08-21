
import geopandas as gpd
import matplotlib.pyplot as plt

geo_df_path = 'geo_df.gpkg'
geo_df = gpd.read_file(geo_df_path)
europe_shapefile_path = 'europe.gpkg'
europe_shapefile = gpd.read_file(europe_shapefile_path)

grassland_geo_df = geo_df[geo_df['LC0_Desc'] == 'Grassland']
cropland_geo_df = geo_df[geo_df['LC0_Desc'] == 'Cropland']

fig, ax = plt.subplots(figsize=(10, 10))
europe_shapefile.plot(ax=ax, color='lightgrey')
grassland_geo_df.plot(ax=ax, marker='.', color='green', markersize=5, label='Grassland')
cropland_geo_df.plot(ax=ax, marker='.', color='orange', markersize=5, label='Cropland')

ax.legend()
plt.savefig('plots/plot27.png')
