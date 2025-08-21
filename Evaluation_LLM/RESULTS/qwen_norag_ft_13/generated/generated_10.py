
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")
countries_df = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter countries within Europe
europe_df = europe_df[europe_df["Continent"] == "Europe"]

# Plot Europe
fig, ax = plt.subplots(figsize=(10, 10))
europe_df.plot(ax=ax, color="lightgrey")

# Plot countries
countries_df[countries_df["CONTINENT"] == "Europe"].plot(ax=ax, edgecolor="black", facecolor="none")

# Plot points
geo_df.plot(ax=ax, column="pH_H2O", cmap="coolwarm", markersize=5, legend=True)

# Set title and save
ax.set_title("pH in Water vs Potassium in Europe")
plt.savefig('plots/plot10.png')
plt.close()
