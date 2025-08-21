
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')
countries_df = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Filter the geo_df for nitrogen outliers (N > 4)
nitrogen_outliers = geo_df[geo_df['N'] > 4]

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot Europe shapefile
europe_df.plot(ax=ax, color='lightgrey')

# Plot countries shapefile
countries_df.plot(ax=ax, color='none', edgecolor='black')

# Plot nitrogen outliers
nitrogen_outliers.plot(ax=ax, marker='.', color='red', markersize=5)

# Save the plot
plt.savefig('plots/plot25.png')
