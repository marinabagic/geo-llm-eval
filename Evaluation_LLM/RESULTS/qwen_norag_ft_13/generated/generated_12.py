
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Calculate mean organic carbon
mean_oc = geo_df['OC'].mean()

# Calculate standard error
sem = geo_df['OC'].sem()

# Calculate 95% confidence interval
ci_lower = mean_oc - 1.96 * sem
ci_upper = mean_oc + 1.96 * sem

print(f"Mean Organic Carbon: {mean_oc}")
print(f"95% Confidence Interval: ({ci_lower}, {ci_upper})")
