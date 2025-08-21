
import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoDataFrame and Europe shapefile
geo_df = gpd.read_file("geo_df.gpkg")
europe = gpd.read_file("europe.gpkg")

# Filter GeoDataFrame to keep only European countries
geo_df = geo_df[geo_df["NUTS_0"].isin(europe["Shape_Leng"].str[:2])]

# Plot Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot heatmap of pH values in water
geo_df.plot(ax=ax, column="pH_H2O", cmap="coolwarm", legend=True, markersize=10)

# Save plot
plt.savefig('plots/plot24.png')
plt.close()
