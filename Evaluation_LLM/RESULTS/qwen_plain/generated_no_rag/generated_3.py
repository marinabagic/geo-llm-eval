
import geopandas as gpd
from scipy import stats

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_df = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
ax = europe_df.plot(color='lightgrey', figsize=(10, 10))

# Plot the points from geo_df
geo_df.plot(ax=ax, marker='.', markersize=1)

# Save the plot
ax.figure.savefig('plots/plot3.png')

# Filter data for Austria and France
austria_data = geo_df[geo_df['NUTS_0'] == 'AT']['N']
france_data = geo_df[geo_df['NUTS_0'] == 'FR']['N']

# Perform t-test
t_stat, p_value = stats.ttest_ind(austria_data, france_data)

print(f"T-statistic: {t_stat}, P-value: {p_value}")
