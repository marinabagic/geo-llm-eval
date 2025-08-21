
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('LUCAS.csv')
df = df[df["Depth"] == "0-20 cm"]
df["CaCO3"] = pd.to_numeric(df["CaCO3"], errors="coerce")

plt.figure(figsize=(10, 6))
plt.hist(df["CaCO3"].dropna(), bins=30, color="skyblue", edgecolor="black")
plt.title("Histogram of Carbonate Content (0-20 cm)")
plt.xlabel("CaCO3")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig('plots/plot13.png')
plt.close()
