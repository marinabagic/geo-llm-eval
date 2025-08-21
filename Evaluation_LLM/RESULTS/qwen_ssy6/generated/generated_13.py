
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('LUCAS.csv')
df = df[df["Depth"] == "0-20 cm"]
df["CaCO3"] = pd.to_numeric(df["CaCO3"], errors="coerce")

plt.figure(figsize=(10, 6))
plt.hist(df["CaCO3"].dropna(), bins=30, edgecolor="black")
plt.title("Histogram of Carbonate Content (0-20 cm)")
plt.xlabel("CaCO3 (g/kg)")
plt.ylabel("Frequency")
plt.savefig('plots/plot13.png')
