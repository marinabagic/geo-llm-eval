
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_file("geo_df.gpkg")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")
europe = gpd.read_file("europe.gpkg")

# Filter for Germany
df = df[df["Country"] == "Germany"]

# Compute average pH_H2O per NUTS2 region
df["NUTS_2"] = df["NUTS_2"].str[:5]  # Ensure correct format
df_grouped = df.groupby("NUTS_2").agg({"pH_H2O": "mean"}).reset_index()

# Merge with country shapefile
germany = countries[countries["NAME"] == "Germany"]
germany = germany.to_crs(df_grouped.crs)
germany["NUTS_2"] = germany["ISO_A3"] + germany["NAME"].str[-3:]
germany = germany.merge(df_grouped, on="NUTS_2", how="left")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
germany.plot(ax=ax, column="pH_H2O", legend=True, cmap="viridis", missing_kwds={"color": "lightgrey"})

ax.set_title("Average pH_H2O per NUTS2 Region in Germany")
plt.tight_layout()
plt.savefig('plots/plot40.png')
plt.close()
