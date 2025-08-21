
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the Europe shapefile
europe_gdf = gpd.read_file('europe.gpkg')

# Load the countries shapefile
countries_gdf = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Filter the countries shapefile to include only Italy
italy_gdf = countries_gdf[countries_gdf['NAME'] == 'Italy']

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Filter the GeoDataFrame to include only points in Italy
italy_points_gdf = geo_df[geo_df['NUTS_0'] == 'IT']

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot Italy shapefile
italy_gdf.plot(ax=ax, color='none', edgecolor='black')

# Plot points in Italy, colored by LC0_Desc category
italy_points_gdf.plot(ax=ax, column='LC0_Desc', legend=True, markersize=5, marker='.')

# Save the plot
plt.savefig('plots/plot41.png')
