
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
df = pd.read_file("geo_df.gpkg")
europe = gpd.read_file("europe.gpkg")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")

# Filter European countries
europe["country"] = europe["NAME"]
europe["iso_code"] = europe["ISO_A2"]
countries = countries[countries["iso_code"].isin(europe["iso_code"])]

# Plot Europe
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")

# Plot countries
countries.plot(ax=ax, edgecolor="black", facecolor="none")

# Plot points
df.plot(ax=ax, x="TH_LONG", y="TH_LAT", column="pH_H2O", cmap="viridis", legend=True, markersize=5)

# Save plot
plt.savefig('plots/plot1.png')
plt.close()

# Find general land cover class with highest average soil pH in water
average_ph_h2o = df.groupby("LC0_Desc")["pH_H2O"].mean().sort_values(ascending=False)
highest_ph_class = average_ph_h2o.idxmax()
highest_ph_value = average_ph_h2o.max()

print(f"The general land cover class with the highest average soil pH in water is '{highest_ph_class}' with a value of {highest_ph_value:.2f}.")
