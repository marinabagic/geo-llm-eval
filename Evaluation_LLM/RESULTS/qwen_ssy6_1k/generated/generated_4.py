
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('LUCAS.csv')
sns.histplot(df["P"], kde=True)
plt.title("Histogram of Phosphorus Content")
plt.xlabel("Phosphorus (P)")
plt.ylabel("Frequency")
plt.savefig('plots/plot4.png')
