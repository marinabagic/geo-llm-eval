
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
europe = gpd.read_file("europe.gpkg")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")
df = gpd.read_file("geo_df.gpkg")

# Filter European countries
europe_countries = countries[countries["CONTINENT"] == "Europe"]

# Filter df for spruce and pine dominated forests
spruce_forest = df[df["LC1_Desc"] == "Spruce dominated coniferous woodland"]
pine_forest = df[df["LC1_Desc"] == "Pine dominated coniferous woodland"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))

europe.plot(ax=ax, color="lightgrey")
europe_countries.plot(ax=ax, color="white", edgecolor="black")
spruce_forest.plot(ax=ax, color="green", markersize=5, label="Spruce Forest")
pine_forest.plot(ax=ax, color="red", markersize=5, label="Pine Forest")

ax.set_title("Spruce vs Pine Dominated Forests in Europe")
ax.legend()

plt.savefig('plots/plot28.png')
plt.close()
