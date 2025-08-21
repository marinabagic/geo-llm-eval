
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
countries_df.plot(ax=ax, color="white", edgecolor="black")

# Plot points
geo_df.plot(ax=ax, color="blue", markersize=5)

# Set limits to Europe
ax.set_xlim(europe_df.total_bounds[0], europe_df.total_bounds[2])
ax.set_ylim(europe_df.total_bounds[1], europe_df.total_bounds[3])

# Save plot
plt.savefig('plots/plot4.png')
plt.close()

# Histogram of phosphorus content
plt.figure(figsize=(10, 6))
plt.hist(geo_df["P"], bins=30, density=True, alpha=0.6, color="green", edgecolor="black")
plt.title("Histogram of Phosphorus Content with KDE")
plt.xlabel("Phosphorus (P)")
plt.ylabel("Density")

# Kernel Density Estimate
from scipy.stats import gaussian_kde
kde = gaussian_kde(geo_df["P"].dropna())
x = np.linspace(geo_df["P"].min(), geo_df["P"].max(), 1000)
plt.plot(x, kde(x), color="red", linewidth=2)

# Save plot
plt.savefig('plots/plot4.png')
plt.close()
