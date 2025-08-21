
import geopandas as gpd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Perform KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
geo_df['cluster'] = kmeans.fit_predict(geo_df[['TH_LAT', 'TH_LONG']])

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color='lightgrey')

# Plot the clustered points
geo_df.plot(ax=ax, column='cluster', markersize=5, legend=True)

# Save the plot
plt.savefig('plots/plot30.png')
