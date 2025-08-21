
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')

# Plot the sampling locations colored by detailed land cover category
geo_df.plot(ax=ax, column='LC1_Desc', marker='.', legend=True)

# Save the plot
plt.savefig('plots/plot23.png')
