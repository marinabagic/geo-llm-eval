
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Filter points where organic carbon content is available
available_oc = geo_df[geo_df['OC'].notna()]

fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')
available_oc.plot(ax=ax, marker='.', color='blue')

plt.savefig('plots/plot26.png')
