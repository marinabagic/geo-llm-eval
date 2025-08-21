
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("LUCAS_with_country_info.csv")
df = df.dropna(subset=["pH_H2O", "TH_LAT", "TH_LONG"])

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

# Load European borders
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")
europe = world[world["CONTINENT"] == "Europe"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf.plot(ax=ax, column="pH_H2O", cmap="viridis", markersize=5, legend=True)

ax.set_title("Heatmap of Soil pH in Water Across Europe")
plt.tight_layout()
plt.savefig('plots/plot24.png')
