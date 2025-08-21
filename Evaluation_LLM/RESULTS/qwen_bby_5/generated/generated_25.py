
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load and filter data
df = pd.read_csv("LUCAS_with_country_info.csv")
df["N"] = pd.to_numeric(df["N"], errors="coerce")
df = df[df["N"].notna() & df["IsInEurope"] == True]
df = df[df["N"] > 4]
df = df.dropna(subset=["TH_LAT", "TH_LONG"])

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf.plot(ax=ax, color="red", marker='.', markersize=5, label="N > 4")

# Zoom to bounds of points
ax.set_xlim(gdf.total_bounds[0] - 1, gdf.total_bounds[2] + 1)
ax.set_ylim(gdf.total_bounds[1] - 1, gdf.total_bounds[3] + 1)

plt.title("Nitrogen Outliers (N > 4) in Europe")
plt.legend()
plt.tight_layout()
plt.savefig('plots/plot25.png')
plt.close()
