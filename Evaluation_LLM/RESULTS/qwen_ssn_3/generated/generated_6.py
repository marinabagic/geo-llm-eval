
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Calculate the correlation matrix
corr_matrix = geo_df.corr()

# Plot the heatmap
plt.figure(figsize=(10, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig('plots/plot6.png')
