
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the GeoDataFrame and Europe shapefile
geo_df = gpd.read_file('geo_df.gpkg')
europe_shapefile = gpd.read_file('europe.gpkg')

# Extract the coordinates for clustering
coordinates = geo_df[['TH_LAT', 'TH_LONG']].dropna()

# Perform KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
geo_df['Cluster'] = kmeans.fit_predict(coordinates)

# Plot the Europe shapefile and the clustered points
fig, ax = plt.subplots(figsize=(10, 10))
europe_shapefile.plot(ax=ax, color='lightgrey')
geo_df.plot(ax=ax, marker='.', column='Cluster', cmap='viridis', legend=True)

# Save the plot
plt.savefig('plots/plot30.png')
