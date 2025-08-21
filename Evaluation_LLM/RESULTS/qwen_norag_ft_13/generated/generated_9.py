
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter countries in Europe
europe_df = europe_df[europe_df["Continent"] == "Europe"]

# Plot Europe
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color="lightgrey")

# Plot countries
countries_df.plot(ax=ax, color="white", edgecolor="black")

# Filter and plot points
valid_points = geo_df[geo_df["IsInEurope"] & geo_df["OC"].notna()]
valid_points.plot(ax=ax, column="OC", cmap="viridis", legend=True, markersize=5)

# Set limits to Europe
ax.set_xlim(europe_df.total_bounds[0] - 1, europe_df.total_bounds[2] + 1)
ax.set_ylim(europe_df.total_bounds[1] - 1, europe_df.total_bounds[3] + 1)

# Save plot
plt.savefig('plots/plot9.png')
plt.close()

# ANOVA for OC by Land Cover
anova_results = f_oneway(*[valid_points[valid_points["LC0_Desc"] == lc]["OC"] for lc in valid_points["LC0_Desc"].unique()])
print(f"ANOVA F-statistic: {anova_results.statistic}, p-value: {anova_results.pvalue}")
