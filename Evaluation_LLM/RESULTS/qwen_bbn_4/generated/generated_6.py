
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Select numeric columns for correlation
numeric_cols = geo_df.select_dtypes(include=['number']).columns

# Calculate the correlation matrix
corr_matrix = geo_df[numeric_cols].corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.tight_layout()
plt.savefig('plots/plot6.png')
