
import pandas as pd
import geopandas as gpd

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Calculate average nitrogen per general land cover class
average_nitrogen = geo_df.groupby('LC')['N'].mean()

# Print the result
print(average_nitrogen)
