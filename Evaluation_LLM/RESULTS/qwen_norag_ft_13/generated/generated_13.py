
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_file("geo_df.gpkg")
europe = gpd.read_file("europe.gpkg")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter European countries
europe_countries = countries[countries["CONTINENT"] == "Europe"]

# Plot Europe
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot European countries
europe_countries.plot(ax=ax, color="white", edgecolor="black")

# Plot points
df.plot(ax=ax, column="CaCO3", cmap="viridis", markersize=5, legend=True)

# Set limits to Europe
ax.set_xlim(europe.total_bounds[0], europe.total_bounds[2])
ax.set_ylim(europe.total_bounds[1], europe.total_bounds[3])

# Save plot
plt.savefig('plots/plot13.png')
plt.close()

# Plot histogram of carbonate content (0-20cm)
df["CaCO3"].plot(kind="hist", bins=30, figsize=(10, 6), title="Histogram of Carbonate Content (0-20cm)")
plt.xlabel("CaCO3 (g/kg)")
plt.ylabel("Frequency")

# Save histogram
plt.savefig('plots/plot13.png')
plt.close()
