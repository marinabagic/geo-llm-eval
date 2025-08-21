
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_file("geo_df.gpkg")
europe = gpd.read_file("europe.gpkg")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
countries[countries["CONTINENT"] == "Europe"].plot(ax=ax, color="white", edgecolor="black")

df.plot(ax=ax, column="NUTS_0", legend=True, markersize=5, cmap="tab20")

ax.set_xlim(europe.total_bounds[0] - 1, europe.total_bounds[2] + 1)
ax.set_ylim(europe.total_bounds[1] - 1, europe.total_bounds[3] + 1)

plt.tight_layout()
plt.savefig('plots/plot6.png')
plt.close()
