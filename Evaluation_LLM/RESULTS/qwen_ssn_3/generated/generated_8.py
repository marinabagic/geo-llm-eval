
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Create the boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='LC0_Desc', y='EC', data=geo_df)
plt.title('Boxplot of EC Grouped by Land Use Class')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('plots/plot8.png')
