
import pandas as pd
import geopandas as gpd
from scipy.stats import f_oneway

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Group by land cover and calculate mean organic carbon content
grouped = geo_df.groupby('LC0_Desc')['OC'].mean()

# Perform ANOVA
f_statistic, p_value = f_oneway(*[geo_df[geo_df['LC0_Desc'] == lc]['OC'] for lc in grouped.index])

print(f"F-statistic: {f_statistic}, P-value: {p_value}")
