
import geopandas as gpd
import matplotlib.pyplot as plt

# Read the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Filter points where organic carbon content is available
oc_available_points = geo_df[geo_df['OC'].notna()]

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')
oc_available_points.plot(ax=ax, marker='.', color='blue')

# Save the plot
plt.savefig('plots/plot26.png')
