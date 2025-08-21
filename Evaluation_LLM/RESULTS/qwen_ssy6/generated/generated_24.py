
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')
geo_df.plot(ax=ax, column='pH_H2O', cmap='coolwarm', legend=True, marker='.', linewidth=0)

plt.title('pH Values in Water Across Europe')
plt.savefig('plots/plot24.png')
