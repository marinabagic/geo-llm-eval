
import geopandas as gpd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')
countries_gdf = gpd.read_file('../natural_earth_data/ne_10m_admin_0_countries.shp')

# Filter countries within Europe
europe_countries = countries_gdf[countries_gdf['ISO_A2'].isin(europe_gdf['NUTS_0'])]

# Perform KMeans clustering on the coordinates
kmeans = KMeans(n_clusters=3, random_state=42)
geo_df['Cluster'] = kmeans.fit_predict(geo_df[['TH_LAT', 'TH_LONG']])

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot Europe shapefile
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot countries
europe_countries.plot(ax=ax, edgecolor='black', facecolor='none')

# Plot clustered points
for cluster_id in range(3):
    subset = geo_df[geo_df['Cluster'] == cluster_id]
    subset.plot(ax=ax, marker='.', markersize=5, label=f'Cluster {cluster_id + 1}')

ax.set_title('Europe with 3 Clusters of Coordinates')
ax.legend()

# Save the plot
plt.savefig('plots/plot30.png')
plt.close()
