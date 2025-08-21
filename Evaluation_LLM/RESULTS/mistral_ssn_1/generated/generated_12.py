
import pandas as pd
import scipy.stats as stats
import numpy as np

# Read the GeoDataFrame
geo_df = pd.read_file('geo_df.gpkg')

# Read the Europe Shapefile
europe_shapefile = pd.read_file('europe.gpkg')

# Plot Europe shapefile with lightgrey color
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10,10))
europe_shapefile.plot(ax=ax, color='lightgrey', marker='.', alpha=0.5)

# Calculate confidence interval for mean organic carbon
mean_oc = geo_df['OC'].mean()
sem_oc = stats.sem(geo_df['OC'], nan_policy='omit')
confidence_interval = stats.t.interval(0.95, len(geo_df['OC'].dropna()) - 1, loc=mean_oc, scale=sem_oc)
print("95% Confidence Interval for mean 'OC':", confidence_interval)
