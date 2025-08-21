
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Ensure pH_H2O and K are numeric
geo_df['pH_H2O'] = pd.to_numeric(geo_df['pH_H2O'], errors='coerce')
geo_df['K'] = pd.to_numeric(geo_df['K'], errors='coerce')

# Drop rows with missing values in pH_H2O and K
geo_df = geo_df.dropna(subset=['pH_H2O', 'K'])

# Plot regression plot
plt.figure(figsize=(10, 6))
sns.regplot(x='K', y='pH_H2O', data=geo_df, scatter_kws={'alpha':0.5})
plt.title('Regression Plot of pH in Water vs Potassium')
plt.xlabel('Potassium (K)')
plt.ylabel('pH in Water (pH_H2O)')
plt.tight_layout()
plt.savefig('plots/plot10.png')
