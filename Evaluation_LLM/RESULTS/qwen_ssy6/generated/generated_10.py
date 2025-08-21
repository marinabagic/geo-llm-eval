
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv('LUCAS.csv')
X = df[['pH_H2O']].values
y = df['K'].values
model = LinearRegression()
model.fit(X, y)

sns.scatterplot(x='pH_H2O', y='K', data=df)
plt.plot(df['pH_H2O'], model.predict(X), color='red')
plt.title('Linear Regression: pH in Water vs Potassium')
plt.savefig('plots/plot10.png')
