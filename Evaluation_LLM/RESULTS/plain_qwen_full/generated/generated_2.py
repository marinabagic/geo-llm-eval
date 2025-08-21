
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_gdf = gpd.read_file("europe.gpkg")
countries_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter countries within Europe
europe_countries = countries_gdf[countries_gdf['CONTINENT'] == 'Europe']

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot countries within Europe
europe_countries.plot(ax=ax, edgecolor='black', facecolor='none')

# Calculate average organic carbon content (0-20 cm) by general land cover type
average_oc = geo_df.groupby('LC')['OC'].mean().reset_index()

# Plot points with average organic carbon content
for index, row in average_oc.iterrows():
    ax.scatter([], [], c='blue', label=f'{row["LC"]}: {row["OC"]:.2f}')

# Add legend
ax.legend(title='Average Organic Carbon Content (0-20 cm) by Land Cover Type')

# Save the plot
plt.savefig('plots/plot2.png')
