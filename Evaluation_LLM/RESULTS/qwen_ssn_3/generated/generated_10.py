
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Load the Europe shapefile
europe = gpd.read_file('europe.gpkg')

# Plot the Europe shapefile
fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color='lightgrey')

# Plot the points from the GeoDataFrame
geo_df.plot(ax=ax, marker='.', x='TH_LONG', y='TH_LAT', color='blue')

# Save the plot
plt.savefig('plots/plot10.png')

# Prepare data for regression plot
X = geo_df[['pH_H2O']].values
y = geo_df['K'].values

# Fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Create a scatter plot
sns.scatterplot(x='pH_H2O', y='K', data=geo_df)

# Plot the regression line
plt.plot(geo_df['pH_H2O'], model.predict(X), color='red')

# Add title and labels
plt.title('Linear Regression: pH in Water vs Potassium')
plt.xlabel('pH in Water (pH_H2O)')
plt.ylabel('Potassium (K)')

# Save the regression plot
plt.savefig('plots/plot10.png')
