
import pandas as pd
import numpy as np

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Calculate the mean and standard deviation of EC
ec_mean = geo_df['EC'].mean()
ec_std = geo_df['EC'].std()

# Calculate the Z-scores for EC
geo_df['EC_ZScore'] = (geo_df['EC'] - ec_mean) / ec_std

# Identify outliers based on Z-score (common threshold is |Z| > 3)
outliers = geo_df[np.abs(geo_df['EC_ZScore']) > 3]

# Save the outliers to a new GeoDataFrame
outliers.to_file('outliers.gpkg', driver='GPKG')
