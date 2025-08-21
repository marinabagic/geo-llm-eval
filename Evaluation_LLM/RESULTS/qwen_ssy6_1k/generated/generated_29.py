
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Calculate carbon to nitrogen ratio
geo_df['C_N_Ratio'] = geo_df['OC'] / geo_df['N']

# Filter points where C/N ratio is greater than 10
filtered_points = geo_df[geo_df['C_N_Ratio'] > 10]

fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')
filtered_points.plot(ax=ax, marker='.', color='red')
plt.savefig('plots/plot29.png')
