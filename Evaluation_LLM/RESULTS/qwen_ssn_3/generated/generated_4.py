
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Plot histogram of phosphorus content with KDE
sns.histplot(geo_df['P'], kde=True)
plt.title('Distribution of Phosphorus Content')
plt.xlabel('Phosphorus (P)')
plt.ylabel('Frequency')
plt.savefig('plots/plot4.png')
