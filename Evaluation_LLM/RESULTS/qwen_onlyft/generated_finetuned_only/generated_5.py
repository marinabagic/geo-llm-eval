
import geopandas as gpd
import pandas as pd

# Load GeoDataFrames
geo_df = gpd.read_file("geo_df.gpkg")
europe_df = gpd.read_file("europe.gpkg")

# Filter southern European countries
southern_europe = europe_df[europe_df["NUTS_0"].isin(["ES", "PT", "IT", "CY", "SI", "HR", "AL", "MK", "GR", "TR", "BG", "RO", "HU"])]

# Plot Europe shapefile
ax = southern_europe.plot(color="lightgrey", figsize=(10, 10))

# Filter and plot points within southern Europe
filtered_geo_df = geo_df[geo_df["NUTS_0"].isin(southern_europe["NUTS_0"])]
filtered_geo_df.plot(ax=ax, marker=".", column="pH_CaCl2", legend=True)

# Save plot
ax.set_title("Average pH in Calcium Chloride for Southern European Countries")
plt.savefig('plots/plot5.png', dpi=300)
plt.close()
