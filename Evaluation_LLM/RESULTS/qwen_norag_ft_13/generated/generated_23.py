
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter countries to only those in Europe
europe_df = europe_df[europe_df["Continent"] == "Europe"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))

# Plot Europe shapefile
europe_df.plot(ax=ax, color="lightgrey")

# Plot countries
countries_df.plot(ax=ax, color="white", edgecolor="black")

# Plot sampling locations
geo_df.plot(ax=ax, column="LC1_Desc", legend=True, markersize=5, cmap="tab20")

# Set limits to Europe
ax.set_xlim(europe_df.total_bounds[0] - 1, europe_df.total_bounds[2] + 1)
ax.set_ylim(europe_df.total_bounds[1] - 1, europe_df.total_bounds[3] + 1)

# Save plot
plt.savefig('plots/plot23.png', bbox_inches="tight", dpi=300)
plt.close()
