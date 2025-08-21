
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

# Load dataframe
df = pd.read_csv("LUCAS_with_country_info.csv")
df["EC"] = pd.to_numeric(df["EC"], errors="coerce")

# Filter for valid EC values and points within Europe
df = df[(df["EC"].notna()) & (df["IsInEurope"] == True)]

# Calculate Z-score for EC
df["EC_Z"] = (df["EC"] - df["EC"].mean()) / df["EC"].std()

# Identify outliers
df["EC_Outlier"] = df["EC_Z"].apply(lambda x: np.abs(x) > 3)

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")

# Load countries shapefile
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")
world.plot(ax=ax, color="white", edgecolor="black")
gdf[gdf["EC_Outlier"]].plot(ax=ax, color="red", marker=".", markersize=5, label="EC Outliers")
ax.set_title("EC Z-Score Outliers in Europe")
ax.legend()
plt.tight_layout()
plt.savefig('plots/plot11.png')
plt.close()
