
import geopandas as gpd
import matplotlib.pyplot as plt

geo_df_path = 'geo_df.gpkg'
geo_df = gpd.read_file(geo_df_path)
europe_shapefile_path = 'europe.gpkg'
europe_shapefile = gpd.read_file(europe_shapefile_path)

spruce_forest_geo_df = geo_df[geo_df['LC1_Desc'] == 'Spruce dominated coniferous woodland']
pine_forest_geo_df = geo_df[geo_df['LC1_Desc'] == 'Pine dominated coniferous woodland']

fig, ax = plt.subplots(figsize=(10, 10))
europe_shapefile.plot(ax=ax, color='lightgrey')
spruce_forest_geo_df.plot(ax=ax, marker='.', color='blue', markersize=5, label='Spruce Forest')
pine_forest_geo_df.plot(ax=ax, marker='.', color='red', markersize=5, label='Pine Forest')

plt.legend()
plt.savefig('plots/plot28.png')
