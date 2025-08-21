
import geopandas as gpd
import pandas as pd

# Load GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")

# Plot Europe
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color="lightgrey")

# Filter and plot countries in Europe
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")
countries_in_europe = countries_df[countries_df["CONTINENT"] == "Europe"]
countries_in_europe.plot(ax=ax, color="white", edgecolor="black")

# Sort by K and get top 3 NUTS_2 regions
top_k_regions = geo_df.sort_values(by="K", ascending=False).drop_duplicates(subset="NUTS_2").head(3)

# Plot points for top 3 K regions
top_k_regions.plot(ax=ax, color="red", markersize=10, label="Top 3 K Regions")

# Add legend and title
ax.legend()
ax.set_title("Top 3 NUTS_2 Regions by Potassium Content")

# Save plot
plt.savefig('plots/plot7.png', dpi=300)
plt.close()
