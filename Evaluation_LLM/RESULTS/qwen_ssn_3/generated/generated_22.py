
import geopandas as gpd
import matplotlib.pyplot as plt

# Read the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Filter the points with electrical conductivity larger than 50
filtered_geo_df = geo_df[geo_df['EC'] > 50]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')
filtered_geo_df.plot(ax=ax, marker='.', color='red')

# Save the plot
plt.savefig('plots/plot22.png')
