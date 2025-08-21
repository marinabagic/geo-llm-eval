
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter points with EC > 50
filtered_geo_df = geo_df[geo_df["EC"] > 50]

# Plot Europe
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color="lightgrey")

# Plot countries
countries_df[countries_df["CONTINENT"] == "Europe"].plot(ax=ax, color="white", edgecolor="black")

# Plot filtered points
filtered_geo_df.plot(ax=ax, color="red", markersize=5, label="EC > 50")

# Set limits to Europe
ax.set_xlim(-10, 30)
ax.set_ylim(35, 72)

# Add legend
ax.legend()

# Save plot
plt.savefig('plots/plot22.png')
plt.close()
