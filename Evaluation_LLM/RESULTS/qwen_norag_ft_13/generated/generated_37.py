
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter France
france_df = countries_df[countries_df["NAME"] == "France"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color="lightgrey")
france_df.plot(ax=ax, color="white", edgecolor="black")
geo_df[geo_df["Country"] == "France"].plot(ax=ax, column="LC0_Desc", legend=True, markersize=10)

ax.set_title("Land Cover Categories in France")
plt.savefig('plots/plot37.png')
plt.close()
