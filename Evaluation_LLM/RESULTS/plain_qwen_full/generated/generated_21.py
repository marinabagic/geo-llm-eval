
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the Europe shapefile
europe_gdf = gpd.read_file('europe.gpkg')

# Load the countries shapefile
countries_gdf = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Filter countries within Europe
europe_countries = countries_gdf[countries_gdf['CONTINENT'] == 'Europe']

# Calculate the threshold for top 10% of potassium values
k_threshold = geo_df['K'].quantile(0.9)

# Filter the GeoDataFrame for top 10% of potassium values
top_k_geo_df = geo_df[geo_df['K'] >= k_threshold]

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot Europe shapefile
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot countries within Europe
europe_countries.plot(ax=ax, edgecolor='black', facecolor='none')

# Plot points with top 10% potassium values
top_k_geo_df.plot(ax=ax, marker='.', color='red', markersize=5)

# Save the plot
plt.savefig('plots/plot21.png')
