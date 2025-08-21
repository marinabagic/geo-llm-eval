
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("LUCAS_with_country_info.csv")
df["pH_H2O"] = pd.to_numeric(df["pH_H2O"], errors="coerce")
df = df.dropna(subset=["pH_H2O", "TH_LAT", "TH_LONG"])

# Filter for Belgium
belgium_df = df[df["Country"] == "Belgium"]

# Calculate bottom 10 percentile of pH_H2O
pH_bottom_10 = belgium_df["pH_H2O"].quantile(0.1)

# Filter points where pH_H2O is in the bottom 10 percentile
belgium_bottom_10 = belgium_df[belgium_df["pH_H2O"] <= pH_bottom_10]

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(belgium_bottom_10, geometry=gpd.points_from_xy(belgium_bottom_10["TH_LONG"], belgium_bottom_10["TH_LAT"]), crs="EPSG:4326")

# Load high-res country borders and clip to Belgium
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")
belgium = world[world["NAME"] == "Belgium"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
belgium.plot(ax=ax, color="lightgrey", edgecolor="black")

gdf.plot(ax=ax, marker='.', color="red", markersize=5)

plt.title("pH_H2O in Bottom 10 Percentile in Belgium")
plt.xlim(2.5, 7)
plt.ylim(48, 52)
plt.tight_layout()
plt.savefig('plots/plot35.png')
plt.close()
