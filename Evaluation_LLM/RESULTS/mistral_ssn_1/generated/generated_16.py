
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

geo_df = pd.read_csv('LUCAS.csv')
europe_shapefile = gpd.read_file('europe.gpkg')

fig, ax = plt.subplots(figsize=(10, 10))
europe_shapefile.plot(ax=ax, color='lightgrey', edgecolor='black')
geo_df.plot(ax=ax, marker='.', markersize=5)
plt.savefig('plots/europe_soil_points.png')
