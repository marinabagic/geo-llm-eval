
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')
ph_water = geo_df['pH_H2O']

fig, ax = plt.subplots(figsize=(10, 10))
sns.kdeplot(ph_water, shade=True, ax=ax)
europe_df.plot(ax=ax, edgecolor='gray', linewidth=0.2)

plt.savefig('plots/ph_water_heatmap.png')
