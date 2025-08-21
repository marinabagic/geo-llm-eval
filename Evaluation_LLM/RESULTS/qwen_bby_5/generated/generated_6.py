
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('LUCAS.csv')
df = df.select_dtypes(include=[float, int])

corr_matrix = df.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.tight_layout()
plt.savefig('plots/plot6.png')
plt.close()
