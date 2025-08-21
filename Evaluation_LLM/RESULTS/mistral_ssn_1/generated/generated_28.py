
import geopandas as gpd
import matplotlib.pyplot as plt

geo_df_path = 'geo_df.gpkg'
geo_df = gpd.read_file(geo_df_path)
europe_shapefile_path = 'europe.gpkg'
europe_shapefile = gpd.read_file(europe_shapefile_path)

spruce_df = geo_df[geo_df['LC1_Desc'] == 'Spruce dominated coniferous woodland']
pine_df = geo_df[geo_df['LC1_Desc'] == 'Pine dominated coniferous woodland']

fig, ax = plt.subplots(figsize=(10, 10))
europe_shapefile.plot(ax=ax, color='lightgrey')
spruce_df.plot(ax=ax, marker='.', markersize=5, color='blue')
pine_df.plot(ax=ax, marker='.', markersize=5, color='red')
plt.savefig('spruce_vs_pine.png')
