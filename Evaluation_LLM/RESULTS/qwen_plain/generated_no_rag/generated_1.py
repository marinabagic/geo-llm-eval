
import geopandas as gpd
import pandas as pd

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
ax = europe_df.plot(color='lightgrey', figsize=(10, 10))

# Plot the points from geo_df
geo_df.plot(ax=ax, marker='.', x='TH_LONG', y='TH_LAT', column='pH_H2O', legend=True)

# Save the plot
ax.figure.savefig('plots/plot1.png')

# Calculate the average soil pH in water for each general land cover class
average_pH = geo_df.groupby('LC')['pH_H2O'].mean()

# Find the general land cover class with the highest average soil pH in water
highest_pH_class = average_pH.idxmax()
highest_pH_value = average_pH.max()

print(f"The general land cover class with the highest average soil pH in water is {highest_pH_class} with an average pH of {highest_pH_value:.2f}.")
