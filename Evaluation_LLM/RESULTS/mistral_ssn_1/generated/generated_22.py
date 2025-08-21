
import geopandas as gpd
import matplotlib.pyplot as plt

geo_df_path = 'geo_df.gpkg'
geo_df = gpd.read_file(geo_df_path)
europe_shapefile_path = 'europe.gpkg'
europe_shapefile = gpd.read_file(europe_shapefile_path)

filtered_geo_df = geo_df[geo_df['EC'] > 50]
fig, ax = plt.subplots(figsize=(10, 10))
europe_shapefile.plot(ax=ax, color='lightgrey')
filtered_geo_df.plot(ax=ax, marker='.', markersize=5, color='blue')
plt.savefig('plots/europe_ec_50.png')
