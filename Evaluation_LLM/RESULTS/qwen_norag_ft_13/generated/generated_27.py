
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
europe = gpd.read_file("europe.gpkg")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")
df = gpd.read_file("geo_df.gpkg")

# Filter European countries
europe_countries = countries[countries["CONTINENT"] == "Europe"]

# Filter df for grassland and cropland
grassland = df[df["LC0_Desc"] == "Grassland"]
cropland = df[df["LC0_Desc"] == "Cropland"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
europe_countries.plot(ax=ax, edgecolor="black", facecolor="none")
grassland.plot(ax=ax, color="green", markersize=5, label="Grassland")
cropland.plot(ax=ax, color="brown", markersize=5, label="Cropland")

ax.set_title("Grassland vs Cropland Locations in Europe")
ax.legend()
plt.tight_layout()
plt.savefig('plots/plot27.png')
plt.close()
