
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('LUCAS.csv')
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig('plots/plot6.png')
