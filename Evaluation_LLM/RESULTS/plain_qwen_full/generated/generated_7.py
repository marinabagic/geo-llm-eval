
import geopandas as gpd
import pandas as pd

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_gdf = gpd.read_file("europe.gpkg")
countries_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Plot Europe shapefile
ax = europe_gdf.plot(color='lightgrey', figsize=(10, 10))

# Plot countries within Europe
countries_gdf[countries_gdf['ISO_A2'].isin(europe_gdf['NUTS_0'])].plot(ax=ax)

# Plot points from geo_df
geo_df.plot(ax=ax, marker='.', x='TH_LONG', y='TH_LAT')

# Save the plot
ax.get_figure().savefig('plots/plot7.png')

# Find top 3 regions (NUTS_2) with highest potassium
top_regions = geo_df.groupby('NUTS_2')['K'].mean().nlargest(3)
print(top_regions)
