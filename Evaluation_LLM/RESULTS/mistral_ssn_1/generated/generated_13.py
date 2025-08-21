
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

europe_shapefile = gpd.read_file('europe.gpkg')
europe_shapefile['color'] = 'lightgrey'

geo_df = pd.read_file('geo_df.gpkg')
carbonate_content = geo_df['CaCO3'].dropna()

plt.hist(carbonate_content, bins=50, marker='.', figsize=(10,10))
plt.xlabel('Carbonate Content (0-20cm)')
plt.ylabel('Frequency')
plt.title('Histogram of Carbonate Content (0-20cm)')
plt.savefig('plots/carbonate_content.png')
