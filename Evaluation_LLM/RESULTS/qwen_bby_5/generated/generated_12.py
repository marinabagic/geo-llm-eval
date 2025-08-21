
import pandas as pd
import geopandas as gpd
import scipy.stats as stats

df = pd.read_file('geo_df.gpkg')
mean_oc = df['OC'].mean()
sem_oc = stats.sem(df['OC'], nan_policy='omit')
confidence_interval = stats.t.interval(0.95, len(df['OC'].dropna()) - 1, loc=mean_oc, scale=sem_oc)
print("95% Confidence Interval for mean 'OC':", confidence_interval)
