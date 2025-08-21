
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_gdf = gpd.read_file("europe.gpkg")
countries_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter points in Austria where 'pH_CaCl2' > 5 and LC0_Desc is 'Woodland'
filtered_points = geo_df[(geo_df['NUTS_0'] == 'AT') & (geo_df['pH_CaCl2'] > 5) & (geo_df['LC0_Desc'] == 'Woodland')]

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot countries shapefile
countries_gdf.plot(ax=ax, color='none', edgecolor='black')

# Plot filtered points
filtered_points.plot(ax=ax, marker='.', color='red')

# Save the plot
plt.savefig('plots/plot32.png')
