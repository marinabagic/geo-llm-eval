
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrame from the specified file
geo_df = gpd.read_file("geo_df.gpkg")

# Filter the GeoDataFrame for Poland and where 'OC' > median
poland_df = geo_df[geo_df["NUTS_0"] == "PL"]
median_oc = poland_df["OC"].median()
poland_df = poland_df[poland_df["OC"] > median_oc]

# Create a GeoDataFrame for the filtered data
poland_gdf = gpd.GeoDataFrame(poland_df, geometry=gpd.points_from_xy(poland_df["TH_LONG"], poland_df["TH_LAT"]), crs="EPSG:4326")

# Load the countries shapefile
world = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")

# Filter the countries shapefile for Poland
poland_shape = world[world["ISO_A2"] == "PL"]

# Load the Europe shapefile
europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")
poland_shape.plot(ax=ax, color="white", edgecolor="black")
poland_gdf.plot(ax=ax, column="LU_DESC", cmap="tab10", markersize=5, marker='.', legend=True)
ax.set_title("OC > Median in Poland (colored by LU_DESC)")
plt.tight_layout()
plt.savefig('plots/plot36.png')
