
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot the points from geo_df
geo_df.plot(ax=ax, marker='.', x='TH_LONG', y='TH_LAT', color='blue')

# Save the plot
plt.savefig('plots/plot13.png')

# Plot histogram of carbonate content (0-20cm)
plt.figure(figsize=(10, 6))
geo_df[geo_df['Depth'] == '0-20 cm']['CaCO3'].hist(bins=20, edgecolor='black')
plt.title('Histogram of Carbonate Content (0-20 cm)')
plt.xlabel('CaCO3')
plt.ylabel('Frequency')
plt.savefig('plots/plot13.png')
