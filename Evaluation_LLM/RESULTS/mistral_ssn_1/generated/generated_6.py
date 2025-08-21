
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the GeoDataFrame
geo_df = pd.read_gpickle('geo_df.gpkg')

# Read the Europe shapefile
europe_shapefile = gpd.read_file('europe.gpkg')

# Plot Europe shapefile
europe_shapefile.plot(color='lightgrey', marker='.', figsize=(10,10))

# Plot correlation matrix heatmap
corr_matrix = geo_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig('plots/correlation_matrix.png')
