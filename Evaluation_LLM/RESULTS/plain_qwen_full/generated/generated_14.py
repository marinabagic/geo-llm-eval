
import geopandas as gpd
import pandas as pd

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')
countries_df = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Plot Europe shapefile
ax = europe_df.plot(color='lightgrey', figsize=(10, 10))

# Plot countries within Europe
countries_in_europe = countries_df[countries_df['ISO_A2'].isin(europe_df['NUTS_0'])]
countries_in_europe.plot(ax=ax)

# Calculate average nitrogen per general land cover class
average_nitrogen_per_lc = geo_df.groupby('LC')['N'].mean().reset_index()

# Save the plot
ax.set_title('Europe and Countries with Average Nitrogen per Land Cover Class')
ax.get_figure().savefig('plots/plot14.png')
