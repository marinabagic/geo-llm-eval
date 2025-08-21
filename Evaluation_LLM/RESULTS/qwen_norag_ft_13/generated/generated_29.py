
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_file("geo_df.gpkg")
europe = gpd.read_file("europe.gpkg")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter points where Carbon to Nitrogen ratio > 10
df["C_N_Ratio"] = df["OC"] / df["N"]
df_filtered = df[df["C_N_Ratio"] > 10]

# Convert to GeoDataFrame
gdf_filtered = gpd.GeoDataFrame(df_filtered, geometry=gpd.points_from_xy(df_filtered["TH_LONG"], df_filtered["TH_LAT"]), crs="EPSG:4326")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
countries[countries["CONTINENT"] == "Europe"].plot(ax=ax, color="white", edgecolor="black")
gdf_filtered.plot(ax=ax, color="red", markersize=5, label="C:N > 10")

ax.set_title("Points with Carbon to Nitrogen Ratio > 10 in Europe")
ax.legend()
plt.tight_layout()

# Save plot
plt.savefig('plots/plot29.png')
plt.close()
