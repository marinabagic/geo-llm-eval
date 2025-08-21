
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
countries_in_europe.plot(ax=ax, color='white', edgecolor='black')

# Plot points from geo_df
geo_df.plot(ax=ax, x='TH_LONG', y='TH_LAT', marker='.', color='red')

# Save the plot
plt.savefig('plots/plot13.png')
plt.close(fig)

# Plot histogram of carbonate content (0-20cm)
fig, ax = plt.subplots(figsize=(10, 10))
geo_df['CaCO3'].hist(ax=ax, bins=20, color='blue', edgecolor='black')
ax.set_title('Histogram of Carbonate Content (0-20cm)')
ax.set_xlabel('Carbonate Content')
ax.set_ylabel('Frequency')

# Save the histogram
plt.savefig('plots/plot13.png')
plt.close(fig)
