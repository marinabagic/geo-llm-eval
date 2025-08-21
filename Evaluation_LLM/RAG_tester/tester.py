import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Load LUCAS data
df = pd.read_csv("LUCAS_with_country_info.csv")
df["N"] = pd.to_numeric(df["N"], errors="coerce")
df = df.dropna(subset=["TH_LAT", "TH_LONG", "N", "LC0_Desc"])

# Convert to GeoDataFrame
geometry = [Point(xy) for xy in zip(df["TH_LONG"], df["TH_LAT"])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326").to_crs(epsg=3035)

# Buffer around Budapest (200 km)
budapest = gpd.GeoSeries([Point(19.0402, 47.4979)], crs="EPSG:4326").to_crs(epsg=3035)
buffer = budapest.buffer(200000).iloc[0]

# Filter data
threshold = gdf["N"].quantile(0.85)
gdf_filtered = gdf[(gdf["N"] > threshold) & (gdf.geometry.within(buffer))]

# Load Europe borders for context
europe = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs(epsg=3035)
europe = europe[europe["CONTINENT"] == "Europe"]

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="white", edgecolor="black")

# Color by LC0_Desc
unique_labels = gdf_filtered["LC0_Desc"].unique()
cmap = cm.get_cmap("tab10", len(unique_labels))
color_dict = {label: cmap(i) for i, label in enumerate(unique_labels)}
colors_list = gdf_filtered["LC0_Desc"].map(color_dict)

gdf_filtered.plot(ax=ax, color=colors_list, markersize=10, marker=".")
for label in unique_labels:
    ax.scatter([], [], color=color_dict[label], label=label)
ax.legend(title="LC0_Desc", loc="lower left")

# Zoom to buffer area
ax.set_title("Top 15% Nitrogen Near Budapest (200 km), Colored by LC0_Desc")
# Add padding to the bounding box
# Add more padding to bounding box (20%)
bounds = gdf_filtered.total_bounds
pad_x = (bounds[2] - bounds[0]) * 0.2
pad_y = (bounds[3] - bounds[1]) * 0.2
ax.set_xlim(bounds[0] - pad_x, bounds[2] + pad_x)
ax.set_ylim(bounds[1] - pad_y, bounds[3] + pad_y)

# Mark Budapest with a star
# Plot a modest Budapest star without adding it to the legend
ax.plot(budapest.geometry.x, budapest.geometry.y, marker="*", color="black", markersize=50)
ax.text(budapest.geometry.x + 10000, budapest.geometry.y + 10000, "Budapest", fontsize=10)


# Title and legend
plt.title("Top 15% Nitrogen Near Budapest (200 km), Colored by LC0_Desc")
ax.legend(title="LC0_Desc", loc="lower left")
plt.tight_layout()
plt.savefig("plots/plot14.png")
plt.show()

