
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the data
df = pd.read_csv('LUCAS.csv')

# Filter out non-numeric values
df = df.dropna(subset=['pH_H2O', 'K'])

# Load the Europe shapefile
europe = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
europe.plot(color='lightgrey', marker='.', figsize=(10,10))

# Prepare the data for regression
X = df[['pH_H2O']].values.reshape(-1, 1)
y = df['K'].values

# Fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Plot the regression line
plt.scatter(df['pH_H2O'], df['K'], color='blue')
plt.plot(df['pH_H2O'], model.predict(X), color='red')
plt.xlabel('pH in water')
plt.ylabel('Potassium')
plt.title('Regression plot of pH in water vs Potassium')
plt.savefig('pH_K_regression.png')
