
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("LUCAS.csv")
df["pH_H2O"] = pd.to_numeric(df["pH_H2O"], errors="coerce")

means = []
for _ in range(1000):
    sample = df["pH_H2O"].dropna().sample(n=30, random_state=np.random.randint(0, 1000))
    means.append(sample.mean())

plt.figure(figsize=(10, 10))
plt.hist(means, bins=30, color="skyblue", edgecolor="black")
plt.title("Sampling Distribution of Mean pH in Water (n=30, 1000 Samples)")
plt.xlabel("Mean pH in Water")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig('plots/plot15.png')
plt.close()
