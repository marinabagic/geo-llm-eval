
import geopandas as gpd
import pandas as pd

# Load data
df = pd.read_file("geo_df.gpkg")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")
europe = gpd.read_file("europe.gpkg")

# Filter for Croatia and OC below 20
df_croatia = df[(df["Country"] == "Croatia") & (df["OC"] < 20)]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
countries.plot(ax=ax, color="white", edgecolor="black")
df_croatia.plot(ax=ax, color="red", markersize=5, label="OC < 20")

# Zoom to Croatia
ax.set_xlim(df_croatia["TH_LONG"].min() - 1, df_croatia["TH_LONG"].max() + 1)
ax.set_ylim(df_croatia["TH_LAT"].min() - 1, df_croatia["TH_LAT"].max() + 1)

# Legend and title
ax.legend()
ax.set_title("OC < 20 in Croatia")

# Save plot
plt.savefig('plots/plot31.png')
plt.close()
