
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

europe_shapefile = gpd.read_file('europe.gpkg')
europe_shapefile['color'] = 'lightgrey'

geo_df = pd.read_csv('LUCAS.csv')
geo_df.set_index('NUTS_0', inplace=True)

boxplot_data = geo_df.groupby('LC')['EC'].boxplot(figsize=(10,10), marker='.')
plt.title('Boxplot of EC grouped by land use class')
plt.savefig('plots/boxplot_ec.png')
