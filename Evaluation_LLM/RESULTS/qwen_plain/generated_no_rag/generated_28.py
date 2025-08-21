
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Filter the GeoDataFrame for spruce and pine dominated forests
spruce_forests = geo_df[geo_df['LC1_Desc'] == 'Spruce dominated coniferous woodland']
pine_forests = geo_df[geo_df['LC1_Desc'] == 'Pine dominated coniferous woodland']

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')

# Plot spruce and pine dominated forests
spruce_forests.plot(ax=ax, marker='.', color='green', label='Spruce Dominated Forests')
pine_forests.plot(ax=ax, marker='.', color='red', label='Pine Dominated Forests')

# Add legend and title
ax.legend()
ax.set_title('Spruce vs Pine Dominated Forests in Europe')

# Save the plot
plt.savefig('plots/plot28.png')
