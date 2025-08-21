
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")

# Filter top 10% of potassium values
threshold = geo_df['K'].quantile(0.9)
filtered_df = geo_df[geo_df['K'] > threshold]

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')

# Plot filtered GeoDataFrame
filtered_df.plot(ax=ax, column='K', marker='.', legend=True)

# Save plot
plt.savefig('plots/plot21.png')
plt.close()
