
import pandas as pd
import geopandas as gpd
from scipy.stats import f_oneway

# Load the GeoDataFrames
geo_df = gpd.read_file('geo_df.gpkg')
europe_gdf = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
ax = europe_gdf.plot(color='lightgrey', figsize=(10, 10))

# Plot the points from geo_df
geo_df.plot(ax=ax, marker='.', markersize=5, color='red')

# Save the plot
ax.get_figure().savefig('plots/plot9.png')

# Calculate ANOVA for organic carbon content by land cover
anova_result = f_oneway(*[geo_df[geo_df['LC'] == lc]['OC'] for lc in geo_df['LC'].unique()])

print("ANOVA F-statistic:", anova_result.statistic)
print("ANOVA P-value:", anova_result.pvalue)
