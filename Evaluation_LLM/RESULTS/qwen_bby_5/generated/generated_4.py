
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('LUCAS.csv')
df["P"] = pd.to_numeric(df["P"], errors="coerce")

plt.figure(figsize=(10, 6))
plt.hist(df["P"].dropna(), bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
plt.plot(df["P"].dropna(), stats.kde.gaussian_kde(df["P"].dropna)(df["P"].dropna()), color='r', linewidth=2)
plt.title("Histogram of Phosphorus Content with KDE")
plt.xlabel("Phosphorus (P)")
plt.ylabel("Density")
plt.grid(True)
plt.tight_layout()
plt.savefig('plots/plot4.png')
plt.close()
