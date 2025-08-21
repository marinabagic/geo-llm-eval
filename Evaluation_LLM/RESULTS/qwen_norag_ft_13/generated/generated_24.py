
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter European countries
europe_countries = countries_df[countries_df["CONTINENT"] == "Europe"]

# Plot Europe
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color="lightgrey")

# Plot European countries
europe_countries.plot(ax=ax, color="white", edgecolor="black")

# Plot points with heatmap
geo_df.plot(ax=ax, column="pH_H2O", cmap="viridis", markersize=5, legend=True)

# Set title and save plot
ax.set_title("pH Values in Water on Europe Map")
plt.savefig('plots/plot24.png', dpi=300)
plt.close()
