
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_gdf = gpd.read_file("europe.gpkg")
countries_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter the geo_df for entries in July 2018
july_2018_df = geo_df[geo_df['SURVEY_DATE'].str.contains('07-18')]

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot countries shapefile
countries_gdf.plot(ax=ax, color='none', edgecolor='black')

# Plot points with different colors based on LC0_Desc
july_2018_df.plot(ax=ax, column='LC0_Desc', legend=True, markersize=5, marker='.')

# Save the plot
plt.savefig('plots/plot33.png')
