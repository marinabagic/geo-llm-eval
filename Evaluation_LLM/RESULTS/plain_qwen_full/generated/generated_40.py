
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_gdf = gpd.read_file("europe.gpkg")
countries_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter the data for Germany
germany_gdf = countries_gdf[countries_gdf['ISO_A2'] == 'DE']

# Merge Germany's geometry with the geo_df to get NUTS2 regions
germany_with_nuts2 = gpd.sjoin(geo_df, germany_gdf, how="inner", predicate="within")

# Calculate the average pH_H2O per NUTS2 region
average_pH_H2O = germany_with_nuts2.groupby('NUTS_2')['pH_H2O'].mean().reset_index()

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot the countries shapefile
countries_gdf.plot(ax=ax, color='none', edgecolor='black')

# Plot the average pH_H2O per NUTS2 region
germany_gdf.merge(average_pH_H2O, on='NUTS_2').plot(column='pH_H2O', ax=ax, legend=True, cmap='viridis', markersize=0)

# Save the plot
plt.savefig('plots/plot40.png')
