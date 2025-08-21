
import pandas as pd

# Read the GeoDataFrame
geo_df_path = 'geo_df.gpkg'
geo_df = pd.read_file(geo_df_path)

# Group by NUTS_2 and calculate the mean potassium (K)
mean_potassium_by_region = geo_df.groupby('NUTS_2')['K'].mean()

# Get the top 3 regions with the highest potassium
top_3_regions = mean_potassium_by_region.nlargest(3)

# Print the top 3 regions
print(top_3_regions)
