
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_file("geo_df.gpkg")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")
europe = gpd.read_file("europe.gpkg")

# Filter for Italy
df = df[df["Country"] == "Italy"]

# Plot Europe
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot Italy with categories
countries[countries["NAME"] == "Italy"].plot(ax=ax, color="white", edgecolor="black")
df.plot(ax=ax, column="LC0_Desc", legend=True, markersize=5)

# Set limits
ax.set_xlim(6, 19)
ax.set_ylim(36, 48)

# Save plot
plt.savefig('plots/plot41.png')
plt.close()
