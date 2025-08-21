
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot GeoDataFrame
geo_df.plot(ax=ax, column="OC", legend=True, marker=".", cmap="viridis")

# Set title and save plot
ax.set_title("Organic Carbon Content by Land Cover")
plt.savefig('plots/plot9.png')
plt.close()

# ANOVA test
anova_result = stats.f_oneway(
    geo_df[geo_df["LC0_Desc"] == "Woodland"]["OC"],
    geo_df[geo_df["LC0_Desc"] == "Cropland"]["OC"],
    geo_df[geo_df["LC0_Desc"] == "Grassland"]["OC"]
)

print("ANOVA F-statistic:", anova_result.statistic)
print("ANOVA P-value:", anova_result.pvalue)
