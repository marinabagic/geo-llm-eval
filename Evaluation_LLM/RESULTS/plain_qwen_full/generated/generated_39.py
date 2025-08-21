
import geopandas as gpd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_gdf = gpd.read_file("europe.gpkg")
countries_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter the data for Spain
spain_gdf = countries_gdf[countries_gdf['NAME'] == 'Spain']

# Perform KMeans clustering on OC and K values
kmeans = KMeans(n_clusters=3, random_state=42)
geo_df['Cluster'] = kmeans.fit_predict(geo_df[['OC', 'K']])

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot Europe shapefile
europe_gdf.plot(ax=ax, color='lightgrey')

# Plot Spain shapefile
spain_gdf.plot(ax=ax, color='none', edgecolor='black')

# Plot the clustered points
geo_df.plot(ax=ax, column='Cluster', markersize=5, legend=True)

# Save the plot
plt.savefig('plots/plot39.png')
