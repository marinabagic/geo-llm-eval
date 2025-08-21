
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")
europe = gpd.read_file("europe.gpkg")

# Filter for Poland and OC > median
poland = countries[countries["NAME"] == "Poland"]
geo_df["OC"] = pd.to_numeric(geo_df["OC"], errors="coerce")
median_oc = geo_df["OC"].median()
poland_points = geo_df[(geo_df["NUTS_0"] == "PL") & (geo_df["OC"] > median_oc)]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
poland.plot(ax=ax, color="white", edgecolor="black")
poland_points.plot(ax=ax, column="LU1_Desc", legend=True, markersize=5)

ax.set_title("Poland - OC > Median, Colored by LU1_Desc")
plt.savefig('plots/plot36.png')
plt.close()
