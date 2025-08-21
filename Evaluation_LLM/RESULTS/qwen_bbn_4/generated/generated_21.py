
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load and filter data
df = pd.read_csv("LUCAS_with_country_info.csv")
df["K"] = pd.to_numeric(df["K"], errors="coerce")
df = df[df["K"].notna()]
df = df[df["TH_LONG"].notna() & df["TH_LAT"].notna()]
df = df[df["K"] > df["K"].quantile(0.9)]

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

# Load high-res countries shapefile
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")
europe = world[world["CONTINENT"] == "Europe"].explode(index_parts=True)

# Optional: filter out small islands (keep large landmasses only)
europe["area"] = europe.geometry.area
europe_mainland = europe[europe["area"] > 1]  # Keep mainland

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe_mainland.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf.plot(ax=ax, color="red", markersize=5, marker='.', label="K > 90th Percentile")

# Zoom to bounds of points
ax.set_xlim(gdf.total_bounds[0] - 1, gdf.total_bounds[2] + 1)
ax.set_ylim(gdf.total_bounds[1] - 1, gdf.total_bounds[3] + 1)

plt.title("Top 10% Potassium Values in Europe")
plt.legend()
plt.tight_layout()
plt.savefig('plots/plot21.png')
