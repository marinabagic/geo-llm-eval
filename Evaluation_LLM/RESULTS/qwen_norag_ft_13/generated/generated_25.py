
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_file("geo_df.gpkg")
europe = gpd.read_file("europe.gpkg")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter nitrogen outliers
df = df[df["N"] > 4]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
countries[countries["CONTINENT"] == "Europe"].plot(ax=ax, color="white", edgecolor="black")
df.plot(ax=ax, x="TH_LONG", y="TH_LAT", color="red", markersize=5, label="N > 4")

ax.set_title("Nitrogen Outliers (N > 4) in Europe")
ax.legend()
plt.tight_layout()
plt.savefig('plots/plot25.png')
plt.close()
