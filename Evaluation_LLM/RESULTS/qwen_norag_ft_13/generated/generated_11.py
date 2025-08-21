
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Calculate Z-score for EC
geo_df['EC_Z'] = (geo_df['EC'] - geo_df['EC'].mean()) / geo_df['EC'].std()

# Identify outliers
outliers = geo_df[abs(geo_df['EC_Z']) > 3]

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Load countries shapefile
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")
countries = countries[countries["CONTINENT"] == "Europe"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
countries.plot(ax=ax, color="white", edgecolor="black")
outliers.plot(ax=ax, color="red", markersize=10)

ax.set_xlim(europe.total_bounds[0] - 1, europe.total_bounds[2] + 1)
ax.set_ylim(europe.total_bounds[1] - 1, europe.total_bounds[3] + 1)

plt.savefig('plots/plot11.png')
plt.close()
