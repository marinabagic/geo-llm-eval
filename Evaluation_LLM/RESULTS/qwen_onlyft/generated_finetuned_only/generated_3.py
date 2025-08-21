
import geopandas as gpd
import pandas as pd
from scipy.stats import ttest_ind

# Load GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")

# Filter for Austria and France
austria_df = geo_df[geo_df["NUTS_0"] == "AT"]
france_df = geo_df[geo_df["NUTS_0"] == "FR"]

# Extract nitrogen content
austria_n = austria_df["N"].dropna()
france_n = france_df["N"].dropna()

# Perform t-test
t_stat, p_value = ttest_ind(austria_n, france_n)

# Print result
print(f"T-statistic: {t_stat}, P-value: {p_value}")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color="lightgrey")
austria_df.plot(ax=ax, markersize=5, color="red", label="Austria")
france_df.plot(ax=ax, markersize=5, color="blue", label="France")
ax.set_title("Nitrogen Content in Austria and France")
ax.legend()
plt.savefig('plots/plot3.png')
plt.close()
