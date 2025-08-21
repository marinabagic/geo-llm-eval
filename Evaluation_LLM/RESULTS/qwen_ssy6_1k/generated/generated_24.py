
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey', edgecolor='black')

if not geo_df.empty:
    geo_df.plot(ax=ax, column='pH_H2O', legend=True, cmap='coolwarm', markersize=5, alpha=0.7)

plt.title('pH Values in Water across Europe')
plt.savefig('plots/plot24.png')
