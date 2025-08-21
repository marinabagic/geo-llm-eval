
import pandas as pd
import geopandas as gpd

# Read the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Read the Europe Shapefile
europe_shp = gpd.read_file('europe.gpkg')

# Plot Europe shapefile with lightgrey color
europe_shp.plot(color='lightgrey')

# Set marker for the GeoDataFrame
geo_df['marker'] = '.'

# Plot the GeoDataFrame with marker
geo_df.plot(marker='.', figsize=(10,10))

# Calculate average nitrogen per general land cover class
grouped = geo_df.groupby('LC')['N'].mean()
print(grouped)
