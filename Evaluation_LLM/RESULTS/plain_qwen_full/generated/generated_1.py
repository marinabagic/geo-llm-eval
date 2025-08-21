
import geopandas as gpd
import pandas as pd

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')
countries_gdf = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Plot Europe shapefile
ax = europe_gdf.plot(color='lightgrey', figsize=(10, 10))

# Plot countries within Europe
countries_gdf[countries_gdf['ISO_A2'].isin(europe_gdf['NUTS_0'])].plot(ax=ax)

# Plot points from geo_df
geo_df.plot(ax=ax, marker='.', x='TH_LONG', y='TH_LAT', color='red')

# Save the plot
ax.figure.savefig('plots/plot1.png')

# Calculate average soil pH in water for each land cover class
average_pH = geo_df.groupby('LC')['pH_H2O'].mean().reset_index()

# Find the general land cover class with the highest average soil pH in water
highest_pH_class = average_pH.loc[average_pH['pH_H2O'].idxmax(), 'LC']

highest_pH_class
