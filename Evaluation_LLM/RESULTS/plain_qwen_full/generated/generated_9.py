
import pandas as pd
import geopandas as gpd
from scipy.stats import f_oneway

# Load the GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_gdf = gpd.read_file("europe.gpkg")
countries_gdf = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Plot Europe shapefile
ax = europe_gdf.plot(color='lightgrey', figsize=(10, 10))

# Plot countries within Europe
countries_in_europe = countries_gdf[countries_gdf['CONTINENT'] == 'Europe']
countries_in_europe.plot(ax=ax, edgecolor='black')

# Save the plot
ax.set_title('Europe with Country Borders')
ax.get_figure().savefig('plots/plot9.png')

# Calculate ANOVA for organic carbon content by land cover
anova_result = f_oneway(*[geo_df[geo_df['LC'] == lc]['OC'] for lc in geo_df['LC'].unique()])

# Print ANOVA result
print(anova_result)
