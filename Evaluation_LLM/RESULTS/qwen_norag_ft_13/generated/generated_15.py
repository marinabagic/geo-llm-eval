
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("df.csv")
df["pH_H2O"] = pd.to_numeric(df["pH_H2O"], errors="coerce")

# Filter out rows with missing pH_H2O values
df = df.dropna(subset=["pH_H2O"])

# Generate 1000 samples of size 30
samples = [df["pH_H2O"].sample(n=30, replace=True).mean() for _ in range(1000)]

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(samples, bins=30, color="skyblue", edgecolor="black")
plt.title("Sampling Distribution of Mean pH in Water (n=30, 1000 Samples)")
plt.xlabel("Mean pH in Water")
plt.ylabel("Frequency")
plt.grid(True)

# Save plot
plt.savefig('plots/plot15.png')
plt.close()
