
import geopandas as gpd
import matplotlib.pyplot as plt

geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')

organic_carbon_points = geo_df[geo_df['OC'].notnull()]
organic_carbon_points.plot(ax=ax, marker='.', markersize=5)

plt.savefig('plots/organic_carbon_points.png')
