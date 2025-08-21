
import pandas as pd
import geopandas as gpd
from scipy.stats import f_oneway

# Load the GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Perform ANOVA
anova_result = f_oneway(*[geo_df[geo_df["LC"] == lc]["OC"] for lc in geo_df["LC"].unique()])

# Print the ANOVA result
print(anova_result)
