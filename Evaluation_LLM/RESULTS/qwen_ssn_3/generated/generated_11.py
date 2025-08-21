
import pandas as pd
import geopandas as gpd
import scipy.stats as stats

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Calculate Z-score for EC
geo_df['EC_zscore'] = stats.zscore(geo_df['EC'], nan_policy='omit')

# Identify outliers
outliers = geo_df[(geo_df['EC_zscore'] > 3) | (geo_df['EC_zscore'] < -3)]

# Print outliers
print(outliers[['POINTID', 'EC', 'EC_zscore']])
