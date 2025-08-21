
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("LUCAS_with_country_info.csv")

# Filter for valid pH_H2O values
valid_pH = df['pH_H2O'].dropna()

# Parameters for the bootstrap
n_samples = 1000
sample_size = 30

# Bootstrap sampling
bootstrap_means = []
for _ in range(n_samples):
    sample = valid_pH.sample(n=sample_size, replace=True)
    bootstrap_means.append(sample.mean())

# Convert to DataFrame for easier manipulation
bootstrap_means_df = pd.DataFrame(bootstrap_means, columns=['mean_pH'])

# Plot the distribution of the bootstrap means
plt.figure(figsize=(10, 6))
plt.hist(bootstrap_means_df['mean_pH'], bins=30, color='skyblue', edgecolor='black')
plt.title('Sampling Distribution of Mean pH in Water (n=30, 1000 samples)')
plt.xlabel('Mean pH')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('plots/plot15.png')
