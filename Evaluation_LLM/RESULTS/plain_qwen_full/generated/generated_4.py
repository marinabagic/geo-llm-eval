
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')
countries_df = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')

# Plot countries within Europe
countries_in_europe = countries_df[countries_df['ISO_A2'].isin(europe_df['NUTS_0'])]
countries_in_europe.plot(ax=ax, marker='.')

# Plot histogram of phosphorus content with KDE
geo_df['P'].plot(kind='hist', bins=30, alpha=0.5, ax=ax, label='Phosphorus Content')
geo_df['P'].plot(kind='kde', ax=ax, label='KDE')

# Save the plot
plt.legend()
plt.savefig('plots/plot4.png')
