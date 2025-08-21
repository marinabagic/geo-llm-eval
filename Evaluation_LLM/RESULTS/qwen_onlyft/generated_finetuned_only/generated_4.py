
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv("soil_data.csv")
df["P"] = pd.to_numeric(df["P"], errors="coerce")

plt.figure(figsize=(10, 6))
plt.hist(df["P"].dropna(), bins=30, density=True, alpha=0.6, color="g", edgecolor="black")
plt.plot(df["P"].dropna(), df["P"].dropna().apply(lambda x: 0.005), "ro", markersize=2)
plt.title("Histogram of Phosphorus Content with KDE")
plt.xlabel("Phosphorus (P)")
plt.ylabel("Density")
plt.savefig('plots/plot4.png')
plt.close()
