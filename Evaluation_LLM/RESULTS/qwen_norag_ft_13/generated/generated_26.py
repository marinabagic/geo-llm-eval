
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter points where organic carbon content is available
available_oc = geo_df[~geo_df['OC'].isin(['< LOD', '<LOD'])]

# Convert OC to numeric
available_oc['OC'] = pd.to_numeric(available_oc['OC'])

# Plot
fig, ax = plt.subplots(figsize=(10, 10))

# Plot Europe
europe_df.plot(ax=ax, color='lightgrey')

# Plot countries
countries_df.plot(ax=ax, color='white', edgecolor='black')

# Plot points
available_oc.plot(ax=ax, column='OC', cmap='viridis', legend=True, markersize=5)

# Set limits to Europe
ax.set_xlim(-10, 30)
ax.set_ylim(35, 72)

# Save plot
plt.savefig('plots/plot26.png', bbox_inches='tight')
plt.close()
