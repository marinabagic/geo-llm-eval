
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Filter for Woodland areas with pH_H2O < 6
filtered_df = geo_df[(geo_df["LC0_Desc"] == "Woodland") & (geo_df["pH_H2O"] < 6)]

# Load Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
filtered_df.plot(ax=ax, marker=".", markersize=5, color="blue")

# Save plot
plt.savefig('plots/plot19.png', bbox_inches="tight")
plt.close()
