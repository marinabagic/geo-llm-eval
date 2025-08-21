
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter Woodland areas
woodland_df = geo_df[geo_df["LC0_Desc"] == "Woodland"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))

europe_df.plot(ax=ax, color="lightgrey")
countries_df.plot(ax=ax, color="white", edgecolor="black")
woodland_df.plot(ax=ax, color="green", markersize=1)

ax.set_xlim(-10, 30)
ax.set_ylim(35, 72)

plt.savefig('plots/plot18.png')
plt.close()
