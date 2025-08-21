
import geopandas as gpd
import pandas as pd

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
ax = europe_gdf.plot(color='lightgrey', figsize=(10, 10))

# Plot the points from geo_df
geo_df.plot(ax=ax, marker='.', markersize=1)

# Save the plot
ax.get_figure().savefig('plots/plot7.png')

# Find the top 3 regions (NUTS_2) with the highest potassium
top_regions = geo_df.groupby('NUTS_2')['K'].mean().nlargest(3)
print(top_regions)
