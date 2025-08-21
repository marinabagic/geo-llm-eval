
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv('LUCAS.csv')
df.boxplot(column='EC', by='LU')
plt.suptitle('Boxplot of EC grouped by Land Use Class')
plt.title('')
plt.savefig('plots/plot8.png')
