
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('LUCAS.csv')
sample_size = 30
n_simulations = 1000
sample_means = [df['pH_H2O'].sample(sample_size, replace=True).mean() for _ in range(n_simulations)]
sns.histplot(sample_means, kde=True, stat='density', color='blue', label='Sample Means')
sns.kdeplot(np.random.normal(np.mean(sample_means), np.std(sample_means), n_simulations), color='red', label='Normal Distribution')
plt.xlabel('Mean pH_H2O')
plt.ylabel('Density')
plt.title('Sampling Distribution of the Mean pH_H2O')
plt.legend()
plt.savefig('plots/plot15.png')
