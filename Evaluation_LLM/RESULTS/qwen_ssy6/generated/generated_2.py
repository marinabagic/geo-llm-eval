
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv('LUCAS.csv')
df['OC (20-30 cm)'] = pd.to_numeric(df['OC (20-30 cm)'], errors='coerce')
df = df.dropna(subset=['OC (20-30 cm)', 'LC0_Desc'])

avg_oc_by_lc = df.groupby('LC0_Desc')['OC (20-30 cm)'].mean().reset_index()

europe = gpd.read_file('europe.gpkg')
europe.plot(color='lightgrey', figsize=(10, 10))

plt.scatter(avg_oc_by_lc['TH_LONG'], avg_oc_by_lc['TH_LAT'], c=avg_oc_by_lc['OC (20-30 cm)'], cmap='viridis', marker='.', s=50)
plt.colorbar(label='Average OC (20-30 cm)')
plt.title('Average Organic Carbon Content (0-20 cm) by General Land Cover Type')
plt.xlim(europe.total_bounds[0] - 1, europe.total_bounds[2] + 1)
plt.ylim(europe.total_bounds[1] - 1, europe.total_bounds[3] + 1)
plt.savefig('plots/plot2.png')
