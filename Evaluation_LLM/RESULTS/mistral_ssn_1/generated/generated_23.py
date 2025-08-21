
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('LUCAS.csv')
europe_shp = gpd.read_file('europe.gpkg')

# Plot Europe shapefile with light grey color
europe_shp['geometry'] = europe_shp['geometry'].apply(lambda x: x.simplify(0.001))
europe_shp.plot(color='lightgrey', edgecolor='none')

# Plot the sampling locations colored by detailed land cover category
fig, ax = plt.subplots(figsize=(10,10))
colors = df['LC1_Desc'].value_counts().sort_index().to_dict()['Woodland'] * 4
df.plot(column='LC1_Desc', cmap='tab20', ax=ax, marker='.', alpha=0.7, color=[colors])

# Save the plot as png file in the 'plots' directory
plt.savefig('plots/europe_map.png')
