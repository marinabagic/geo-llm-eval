
import pandas as pd
import matplotlib.pyplot as plt

# Load the GeoDataFrame
geo_df = gpd.read_file('geo_df.gpkg')

# Plot histogram of carbonate content (0-20cm)
plt.figure(figsize=(10, 6))
plt.hist(geo_df['CaCO3'], bins=20, edgecolor='black')
plt.title('Histogram of Carbonate Content (0-20cm)')
plt.xlabel('CaCO3 (g/kg)')
plt.ylabel('Frequency')
plt.savefig('plots/plot13.png')
