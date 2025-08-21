
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_gdf = gpd.read_file("europe.gpkg")
countries_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter the countries shapefile to only include Europe
europe_countries = countries_gdf[countries_gdf['CONTINENT'] == 'Europe']

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Filter the geo_df to only include points in Poland where 'OC' > median
poland_points = geo_df[geo_df['NUTS_0'] == 'PL']
median_oc = poland_points['OC'].median()
filtered_points = poland_points[poland_points['OC'] > median_oc]

# Plot the filtered points colored by LU_DESC
filtered_points.plot(ax=ax, marker='.', column='LU1_Desc', legend=True)

# Save the plot
plt.savefig('plots/plot36.png')
