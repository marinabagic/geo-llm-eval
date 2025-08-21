
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the Europe shapefile
europe_gdf = gpd.read_file("europe.gpkg")

# Load the countries shapefile
countries_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter the countries shapefile to only include France
france_gdf = countries_gdf[countries_gdf['ISO_A2'] == 'FR']

# Load the GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Filter the GeoDataFrame to only include points in France
france_points_gdf = geo_df[geo_df['NUTS_0'] == 'FR']

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot France shapefile
france_gdf.plot(ax=ax, color='none', edgecolor='black')

# Plot points in France
france_points_gdf.plot(ax=ax, marker='.', markersize=5, column='LC0_Desc', legend=True)

# Save the plot
plt.savefig('plots/plot37.png')
