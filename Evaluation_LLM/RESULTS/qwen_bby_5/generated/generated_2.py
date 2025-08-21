
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load LUCAS data
df = pd.read_csv("LUCAS.csv")

# Filter for numeric OC and drop missing values
df["OC"] = pd.to_numeric(df["OC"], errors="coerce")
df = df.dropna(subset=["OC", "LC0_Desc"])

# Calculate average OC by land cover type
oc_by_lc = df.groupby("LC0_Desc")["OC"].mean().reset_index()

# Load high-res shapefile for Europe
europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey", edgecolor="black")

# Scatter plot for OC by land cover type
plt.scatter([], [], c=[], cmap="viridis", label="Average OC (0-20 cm)")
scatter = ax.scatter(oc_by_lc["OC"], range(len(oc_by_lc)), c=oc_by_lc["OC"], cmap="viridis")
plt.colorbar(scatter, ax=ax, label="Average OC (0-20 cm)")

# Set labels and title
ax.set_yticks(range(len(oc_by_lc)))
ax.set_yticklabels(oc_by_lc["LC0_Desc"])
plt.xlabel("Average OC (0-20 cm)")
plt.title("Average Organic Carbon Content (0-20 cm) by General Land Cover Type")

plt.tight_layout()
plt.savefig('plots/plot2.png')
plt.close()
