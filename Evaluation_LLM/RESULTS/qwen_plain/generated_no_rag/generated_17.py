
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')

# Filter the points with pH in CaCl2 > 6
filtered_geo_df = geo_df[geo_df['pH_CaCl2'] > 6]

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')
filtered_geo_df.plot(ax=ax, marker='.', markersize=5, color='red')

# Save the plot
plt.savefig('plots/plot17.png')
plt.close(fig)
