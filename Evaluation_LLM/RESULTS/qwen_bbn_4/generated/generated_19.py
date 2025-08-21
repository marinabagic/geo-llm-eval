
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrame
geo_df_path = 'geo_df.gpkg'
geo_df = gpd.read_file(geo_df_path)

# Load Europe shapefile
europe_shapefile_path = 'europe.gpkg'
europe_shapefile = gpd.read_file(europe_shapefile_path)

# Filter GeoDataFrame for Woodland areas with pH in water < 6
filtered_geo_df = geo_df[(geo_df['LC0_Desc'] == 'Woodland') & (geo_df['pH_H2O'] < 6)]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe_shapefile.plot(ax=ax, color='lightgrey')
filtered_geo_df.plot(ax=ax, marker='.', color='green', markersize=5)

# Save the plot
plt.savefig('plots/plot19.png')
