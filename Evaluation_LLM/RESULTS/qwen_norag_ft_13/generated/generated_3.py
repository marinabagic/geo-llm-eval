
import pandas as pd
import geopandas as gpd
from scipy import stats

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Load Europe shapefile
europe_df = gpd.read_file("europe.gpkg")

# Load countries shapefile
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter GeoDataFrame for Austria and France
australia_df = geo_df[geo_df["Country"] == "Austria"]
france_df = geo_df[geo_df["Country"] == "France"]

# Perform t-test
t_test_result = stats.ttest_ind(australia_df["N"], france_df["N"])

# Print t-test result
print(t_test_result)
