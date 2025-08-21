
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Filter data for Germany
germany_data = geo_df[geo_df['NUTS_0'] == 'DE']

# Group by NUTS2 region and compute average pH_H2O
average_pH_H2O = germany_data.groupby('NUTS_2')['pH_H2O'].mean().reset_index()

# Load the countries shapefile
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter for Germany
germany_shape = countries[countries['ISO_A2'] == 'DE']

# Merge the average pH_H2O data with the Germany shapefile
germany_shape = germany_shape.merge(average_pH_H2O, left_on='ADM0_A3', right_on='NUTS_2', how='left')

# Plot the choropleth map
fig, ax = plt.subplots(figsize=(10, 10))
germany_shape.plot(column='pH_H2O', ax=ax, legend=True, cmap='viridis', missing_kwds={"color": "lightgrey"}, edgecolor='black')

# Set title and labels
ax.set_title('Average pH_H2O per NUTS2 Region in Germany')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# Save the plot
plt.savefig('plots/plot40.png')
