
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')
countries_gdf = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Filter the geo_df for Slovakia and where 'K' is above its 85th percentile
slovakia_geo_df = geo_df[geo_df['NUTS_0'] == 'SK']
k_percentile = slovakia_geo_df['K'].quantile(0.85)
filtered_slovakia_geo_df = slovakia_geo_df[slovakia_geo_df['K'] > k_percentile]

# Plot Europe shapefile
ax = europe_gdf.plot(color='lightgrey', figsize=(10, 10))

# Plot countries shapefile
countries_gdf.plot(ax=ax, color='none', edgecolor='black')

# Plot filtered points in Slovakia
filtered_slovakia_geo_df.plot(ax=ax, marker='.', color='red')

# Save the plot
plt.savefig('plots/plot34.png')
