
import pandas as pd
import geopandas as gpd
from scipy import stats

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_gdf = gpd.read_file("europe.gpkg")
countries_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Plot Europe shapefile
ax = europe_gdf.plot(color='lightgrey', figsize=(10, 10))

# Plot countries in Europe
countries_gdf[countries_gdf['CONTINENT'] == 'Europe'].plot(ax=ax)

# Filter data for Austria and France
austria_data = geo_df[geo_df['NUTS_0'] == 'AT']
france_data = geo_df[geo_df['NUTS_0'] == 'FR']

# Perform t-test for nitrogen content
t_stat, p_value = stats.ttest_ind(austria_data['N'], france_data['N'])

print(f"T-statistic: {t_stat}, P-value: {p_value}")

# Save the plot
ax.set_title('Europe and Countries')
ax.get_figure().savefig('plots/plot3.png')
