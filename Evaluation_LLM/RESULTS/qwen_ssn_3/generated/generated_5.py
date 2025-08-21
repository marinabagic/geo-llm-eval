
import pandas as pd

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Define the list of southern European countries based on NUTS_0 codes
south_eu = ['PT', 'ES', 'IT', 'GR', 'MT', 'HR', 'SI', 'CY']

# Filter the DataFrame for southern European countries
south_eu_df = geo_df[geo_df['NUTS_0'].isin(south_eu)]

# Calculate the average pH in calcium chloride for southern European countries
avg_ph_cacl2 = south_eu_df['pH_CaCl2'].mean()

# Print the average pH
print(avg_ph_cacl2)
