
import pandas as pd
import geopandas as gpd
from scipy.stats import zscore

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Calculate Z-scores for the 'EC' column
geo_df['EC_zscore'] = zscore(geo_df['EC'])

# Identify outliers based on Z-score (common threshold is |z| > 3)
outliers = geo_df[abs(geo_df['EC_zscore']) > 3]

# Save the outliers to a new GeoDataFrame
outliers.to_file('outliers.gpkg', driver='GPKG')
