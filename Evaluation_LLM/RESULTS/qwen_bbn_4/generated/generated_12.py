
import pandas as pd
import scipy.stats as stats
import geopandas as gpd

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Calculate the mean of organic carbon (OC)
mean_oc = geo_df['OC'].mean()

# Calculate the standard error of the mean for organic carbon (OC)
sem_oc = stats.sem(geo_df['OC'], nan_policy='omit')

# Calculate the 95% confidence interval for the mean organic carbon (OC)
confidence_interval = stats.t.interval(0.95, len(geo_df['OC'].dropna()) - 1, loc=mean_oc, scale=sem_oc)

print("95% Confidence Interval for mean 'OC':", confidence_interval)
