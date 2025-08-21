
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')
countries_gdf = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot Europe shapefile
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot countries within Europe
countries_in_europe = countries_gdf[countries_gdf['ISO_A2'].isin(europe_gdf['NUTS_0'])]
countries_in_europe.plot(ax=ax, marker='.')

# Save the plot
plt.savefig('plots/plot6.png')
