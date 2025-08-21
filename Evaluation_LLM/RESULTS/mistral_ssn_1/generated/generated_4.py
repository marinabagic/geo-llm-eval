
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the GeoDataFrame
geo_df = pd.read_gpkg('geo_df.gpkg')

# Read the Europe shapefile
europe_shp = pd.read_file('europe.shp')

# Plot Europe shapefile
europe_shp.plot(color='lightgrey', marker='.', figsize=(10,10))

# Plot histogram of phosphorus content with KDE
sns.histplot(geo_df['P'], kde=True)
plt.title('Histogram of Phosphorus with KDE')
plt.savefig('plots/phosphorus_kde.png')
