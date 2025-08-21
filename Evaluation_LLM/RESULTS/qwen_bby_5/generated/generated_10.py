
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv("LUCAS_with_country_info.csv")
df["pH_H2O"] = pd.to_numeric(df["pH_H2O"], errors="coerce")
df["K"] = pd.to_numeric(df["K"], errors="coerce")
df = df.dropna(subset=["pH_H2O", "K"])

plt.figure(figsize=(10, 10))
plt.scatter(df["pH_H2O"], df["K"], alpha=0.5)
plt.xlabel("pH in Water")
plt.ylabel("Potassium (K)")
plt.title("Regression Plot of pH in Water vs Potassium")
plt.grid(True)
plt.tight_layout()
plt.savefig('plots/plot10.png')
plt.close()
