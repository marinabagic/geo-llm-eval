
import geopandas as gpd
import pandas as pd

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_gdf = gpd.read_file("europe.gpkg")
countries_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Plot Europe shapefile
ax = europe_gdf.plot(color='lightgrey', figsize=(10, 10))

# Plot countries within Europe
countries_in_europe = countries_gdf[countries_gdf['CONTINENT'] == 'Europe']
countries_in_europe.plot(ax=ax, marker='.')

# Save the plot
ax.get_figure().savefig('plots/plot5.png')

# Calculate average pH in calcium chloride for southern European countries
southern_europe_countries = ['ES', 'PT', 'IT', 'GR', 'CY', 'TR', 'AL', 'MK', 'BG', 'RS', 'ME', 'BA', 'HR', 'SI', 'SK', 'HU', 'RO', 'UA', 'BY', 'LT', 'LV', 'EE', 'FI', 'SE', 'NO', 'DK', 'IS', 'IE', 'GB', 'NL', 'BE', 'LU', 'FR', 'DE', 'CH', 'LI', 'AT', 'CZ', 'PL', 'SK', 'HU', 'RO', 'BG', 'RU']
geo_df_filtered = geo_df[geo_df['NUTS_0'].isin(southern_europe_countries)]
average_pH_CaCl2 = geo_df_filtered['pH_CaCl2'].mean()

print(f"Average pH in calcium chloride for southern European countries: {average_pH_CaCl2}")
