
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_file("geo_df.gpkg")
europe = gpd.read_file("europe.gpkg")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter DataFrame
df = df[(df["OC"] > 20) & (df["LC0_Desc"].isin(["Grassland", "Woodland"]))]

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
countries[countries["CONTINENT"] == "Europe"].plot(ax=ax, color="white", edgecolor="black")
gdf.plot(ax=ax, color="red", markersize=5)

plt.xlim(-10, 30)
plt.ylim(35, 72)
plt.savefig('plots/plot20.png')
plt.close()
