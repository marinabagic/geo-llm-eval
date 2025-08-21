
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load and filter data
df = pd.read_csv("LUCAS_with_country_info.csv")
df["pH_CaCl2"] = pd.to_numeric(df["pH_CaCl2"], errors="coerce")
df = df.dropna(subset=["pH_CaCl2", "TH_LAT", "TH_LONG"])
df = df[df["pH_CaCl2"] > 6]

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf.plot(ax=ax, color="red", marker='.', markersize=5, label="pH_CaCl2 > 6")

plt.title("pH_CaCl2 > 6 in Europe")
plt.legend()
plt.tight_layout()
plt.savefig('plots/plot17.png')
