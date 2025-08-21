
import pandas as pd
import geopandas as gpd
from scipy.stats import t

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Calculate the mean organic carbon (OC)
mean_oc = geo_df['OC'].mean()

# Calculate the standard deviation of organic carbon (OC)
std_oc = geo_df['OC'].std()

# Calculate the number of observations
n = len(geo_df)

# Calculate the degrees of freedom
df = n - 1

# Calculate the t-statistic for a 95% confidence interval
t_stat = t.ppf(0.975, df)

# Calculate the margin of error
margin_of_error = t_stat * (std_oc / (n ** 0.5))

# Calculate the confidence interval
confidence_interval = (mean_oc - margin_of_error, mean_oc + margin_of_error)

print("Mean Organic Carbon:", mean_oc)
print("Confidence Interval:", confidence_interval)
