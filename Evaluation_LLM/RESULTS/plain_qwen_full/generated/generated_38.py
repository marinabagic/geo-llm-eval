
import geopandas as gpd
from shapely.geometry import Point
from shapely.ops import nearest_points

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')
countries_gdf = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Filter countries within Europe
europe_countries = countries_gdf[countries_gdf['CONTINENT'] == 'Europe']

# Find the geometry of London
london_point = Point(-0.1278, 51.5074)

# Calculate the distance from each point to London
geo_df['distance_to_london'] = geo_df.geometry.apply(lambda x: x.distance(london_point))

# Filter points within 100 km of London
points_within_100km = geo_df[geo_df['distance_to_london'] <= 100000]

# Plot Europe and countries
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')
europe_countries.plot(ax=ax, edgecolor='black', facecolor='none')

# Plot points within 100 km of London, colored by LC0_Desc
points_within_100km.plot(ax=ax, column='LC0_Desc', legend=True, markersize=5, marker='.')

# Save the plot
plt.savefig('plots/plot38.png')
