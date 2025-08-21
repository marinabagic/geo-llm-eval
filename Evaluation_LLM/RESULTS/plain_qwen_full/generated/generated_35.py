
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_gdf = gpd.read_file("europe.gpkg")
countries_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter the countries shapefile to only include Europe
europe_gdf = europe_gdf[europe_gdf['NAME'] == 'Europe']

# Filter the geo_df to only include points in Belgium
belgium_gdf = geo_df[geo_df['NUTS_0'] == 'BE']

# Calculate the bottom 10 percentile of pH_H2O in Belgium
bottom_10_percentile = belgium_gdf['pH_H2O'].quantile(0.1)

# Filter the Belgium GeoDataFrame to only include points in the bottom 10 percentile
bottom_10_percentile_gdf = belgium_gdf[belgium_gdf['pH_H2O'] <= bottom_10_percentile]

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot Europe shapefile
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot countries shapefile
countries_gdf.plot(ax=ax, color='none', edgecolor='black')

# Plot points in the bottom 10 percentile
bottom_10_percentile_gdf.plot(ax=ax, marker='.', color='red')

# Save the plot
plt.savefig('plots/plot35.png')
