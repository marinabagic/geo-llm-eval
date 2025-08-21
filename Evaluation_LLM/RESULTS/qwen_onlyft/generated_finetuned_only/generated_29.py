
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrame
geo_df = gpd.read_file("geo_df.gpkg")

# Calculate the carbon to nitrogen ratio
geo_df["C_N_Ratio"] = geo_df["OC"] / geo_df["N"]

# Filter points where the carbon to nitrogen ratio is greater than 10
filtered_df = geo_df[geo_df["C_N_Ratio"] > 10]

# Load the Europe shapefile
europe = gpd.read_file("europe.gpkg")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
filtered_df.plot(ax=ax, marker=".", markersize=5, color="red")

# Save the plot
plt.savefig('plots/plot29.png')
plt.close()
