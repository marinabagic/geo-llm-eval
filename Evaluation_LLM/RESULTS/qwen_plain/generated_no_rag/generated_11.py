
import pandas as pd
from scipy.stats import zscore

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Calculate Z-scores for the 'EC' column
geo_df['EC_ZScore'] = zscore(geo_df['EC'])

# Identify outliers based on Z-score (common threshold is |Z| > 3)
outliers = geo_df[abs(geo_df['EC_ZScore']) > 3]

# Display the outliers
print(outliers[['POINTID', 'EC', 'EC_ZScore']])
