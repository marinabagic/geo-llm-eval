
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = gpd.read_file("geo_df.gpkg")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")
europe = gpd.read_file("europe.gpkg")

# Filter European countries
europe_countries = countries[countries["CONTINENT"] == "Europe"]

# Calculate average OC (0-20 cm) by LC0_Desc
df["OC (20-30 cm)"].fillna(df["OC"], inplace=True)
oc_by_lc = df.groupby("LC0_Desc")["OC (20-30 cm)"].mean().reset_index()

# Plot Europe
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot countries
europe_countries.plot(ax=ax, edgecolor="black", facecolor="none")

# Scatter plot for OC (20-30 cm) by LC0_Desc
for _, row in oc_by_lc.iterrows():
    ax.scatter([], [], c="blue", label=f"{row['LC0_Desc']}: {row['OC (20-30 cm)']:.2f}")

ax.legend(title="Land Cover & Avg OC (20-30 cm)", loc="upper left", bbox_to_anchor=(1, 1))

plt.title("Average Organic Carbon Content (0-20 cm) by General Land Cover Type in Europe")
plt.tight_layout()
plt.savefig('plots/plot2.png')
plt.close()
