
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("LUCAS_with_country_info.csv")
df["pH_H2O"] = pd.to_numeric(df["pH_H2O"], errors="coerce")
df = df.dropna(subset=["pH_H2O", "TH_LAT", "TH_LONG"])

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

# Load European borders
europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf.plot(ax=ax, column="pH_H2O", cmap="plasma", markersize=5, legend=True)

ax.set_xlim(-10, 30)
ax.set_ylim(35, 72)
ax.set_title("Soil pH in Water (pH_H2O) Colored by Value Across Europe")
plt.tight_layout()
plt.savefig('plots/plot24.png')
plt.show()
