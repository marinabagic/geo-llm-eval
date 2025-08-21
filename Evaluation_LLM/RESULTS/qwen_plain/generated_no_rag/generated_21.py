
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')

# Calculate the threshold for the top 10% of potassium values
potassium_threshold = geo_df['K'].quantile(0.9)

# Filter the GeoDataFrame to get the top 10% of potassium values
top_potassium_df = geo_df[geo_df['K'] >= potassium_threshold]

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot the top 10% of potassium values
top_potassium_df.plot(ax=ax, marker='.', markersize=5, color='red', legend=True, label='Top 10% Potassium')

# Save the plot
plt.savefig('plots/plot21.png')
