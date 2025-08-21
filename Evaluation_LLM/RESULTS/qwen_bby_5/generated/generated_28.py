
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("LUCAS_with_country_info.csv")
df = df[df["LC1_Desc"].isin(["Spruce dominated coniferous woodland", "Pine dominated coniferous woodland"])]

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")
gdf[gdf["LC1_Desc"] == "Spruce dominated coniferous woodland"].plot(ax=ax, color="green", markersize=5, label="Spruce")
gdf[gdf["LC1_Desc"] == "Pine dominated coniferous woodland"].plot(ax=ax, color="red", markersize=5, label="Pine")

ax.set_title("Spruce vs Pine Dominated Forests in Europe")
plt.legend()
plt.tight_layout()
plt.savefig('plots/plot28.png')
plt.show()
