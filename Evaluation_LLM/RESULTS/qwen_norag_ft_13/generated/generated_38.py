
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

# Load data
df = pd.read_csv("df.csv")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")
europe = gpd.read_file("europe.gpkg")

# Filter for London
london = countries[countries["NAME"] == "United Kingdom"].centroid.iloc[0]

# Create geometry column from TH_LAT and TH_LONG
df["geometry"] = df.apply(lambda row: Point(row["TH_LONG"], row["TH_LAT"]), axis=1)
gdf = gpd.GeoDataFrame(df, geometry="geometry", crs="EPSG:4326")

# Filter points within 100 km of London
gdf["distance"] = gdf.geometry.distance(london)
filtered_gdf = gdf[gdf["distance"] <= 100000]  # 100 km in meters

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
filtered_gdf.plot(ax=ax, column="LC0_Desc", legend=True, markersize=5)

ax.set_xlim(-10, 3)
ax.set_ylim(49, 60)
plt.tight_layout()
plt.savefig('plots/plot38.png')
plt.close()
