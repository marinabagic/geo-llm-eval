
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv('LUCAS.csv')
df = df.dropna(subset=['EC', 'LU'])

plt.figure(figsize=(10, 10))
sns.boxplot(x='LU', y='EC', data=df)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('plots/plot8.png')
