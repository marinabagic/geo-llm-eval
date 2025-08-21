
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter Europe DataFrame to only include countries in Europe
europe_df = europe_df[europe_df["Continent"] == "Europe"]

# Sort by K in descending order and take top 10%
geo_df_sorted = geo_df.sort_values(by="K", ascending=False)
top_k_count = int(len(geo_df_sorted) * 0.1)
top_k_df = geo_df_sorted.head(top_k_count)

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color="lightgrey")
countries_df.plot(ax=ax, color="white", edgecolor="black")
top_k_df.plot(ax=ax, color="red", markersize=10, marker=".")

# Save plot
plt.savefig('plots/plot21.png')
plt.close()
