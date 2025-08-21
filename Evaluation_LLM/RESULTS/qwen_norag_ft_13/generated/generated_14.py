
import geopandas as gpd
import pandas as pd

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")
europe = gpd.read_file("europe.gpkg")

# Filter European countries
european_countries = countries[countries["CONTINENT"] == "Europe"]

# Plot Europe and countries
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
european_countries.plot(ax=ax, edgecolor="black", facecolor="none")

# Plot points
geo_df.plot(ax=ax, column="N", marker=".", legend=True)

# Save plot
plt.savefig('plots/plot14.png')
plt.close()

# Calculate average nitrogen per land cover class
average_nitrogen = geo_df.groupby("LC0_Desc")["N"].mean().reset_index()
average_nitrogen.columns = ["Land_Cover_Class", "Average_Nitrogen"]

print(average_nitrogen)
