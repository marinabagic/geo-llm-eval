
import pandas as pd
from scipy.stats import t

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Calculate the mean of organic carbon (OC)
mean_oc = geo_df['OC'].mean()

# Calculate the standard error of the mean
std_error = geo_df['OC'].std() / (geo_df['OC'].count() ** 0.5)

# Degrees of freedom
df = geo_df['OC'].count() - 1

# Confidence level
confidence_level = 0.95

# Critical value from t-distribution
critical_value = t.ppf((1 + confidence_level) / 2, df)

# Margin of error
margin_of_error = critical_value * std_error

# Confidence interval
confidence_interval = (mean_oc - margin_of_error, mean_oc + margin_of_error)

print("Confidence Interval for Mean Organic Carbon:", confidence_interval)
