
import pandas as pd
import geopandas as gpd
from scipy import stats

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
ax = europe_gdf.plot(color='lightgrey', figsize=(10, 10))

# Plot the GeoDataFrame points
geo_df.plot(ax=ax, marker='.', x='TH_LONG', y='TH_LAT')

# Save the plot
ax.figure.savefig('plots/plot9.png')

# Perform ANOVA to check if organic carbon content differs by land cover
anova_result = stats.f_oneway(*[geo_df[geo_df['LC'] == lc]['OC'] for lc in geo_df['LC'].unique()])

print(anova_result)
