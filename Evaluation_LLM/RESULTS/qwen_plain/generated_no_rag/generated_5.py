
import geopandas as gpd
import pandas as pd

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Filter southern European countries
southern_countries = ['ES', 'PT', 'IT', 'GR', 'CY', 'AL', 'MK', 'ME', 'BA', 'HR', 'SI', 'SK', 'HU', 'RO', 'BG', 'RS']
filtered_geo_df = geo_df[geo_df['NUTS_0'].isin(southern_countries)]

# Calculate average pH in calcium chloride for southern European countries
average_pH_CaCl2 = filtered_geo_df['pH_CaCl2'].mean()

print(f"Average pH in calcium chloride for southern European countries: {average_pH_CaCl2}")
