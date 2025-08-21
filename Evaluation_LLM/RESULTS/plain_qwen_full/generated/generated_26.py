
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_gdf = gpd.read_file("europe.gpkg")
countries_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter the countries within Europe
europe_countries = countries_gdf[countries_gdf['CONTINENT'] == 'Europe']

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot countries within Europe
europe_countries.plot(ax=ax, edgecolor='black', facecolor='none')

# Filter points where organic carbon content is available
available_oc_points = geo_df[geo_df['OC'].notna()]

# Plot the points
available_oc_points.plot(ax=ax, marker='.', color='red')

# Save the plot
plt.savefig('plots/plot26.png')
