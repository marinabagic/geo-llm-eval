
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('LUCAS.csv')
europe_shapefile = gpd.read_file('europe.gpkg')

# Filter Europe shapefile
europe = europe_shapefile[europe_shapefile['NUTS_0'].isin(['AT', 'BE', 'BG', 'CZ', 'DE', 'DK', 'EL', 'ES', 'FI', 'FR', 'HR', 'HU', 'IE', 'IT', 'CY', 'LU', 'LT', 'LV', 'MT', 'NL', 'PL', 'PT', 'RO', 'SE', 'SI', 'SK', 'UK'])]

# Calculate average organic carbon content (0-20 cm) by general land cover type
grouped = df.groupby(['LC0_Desc', 'LC1_Desc', 'LU1_Desc'])['OC (0-20 cm)'].mean()

# Merge the data with the Europe shapefile
merged = europe.merge(grouped.reset_index(), left_on='LC0_Desc', right_index=True)

# Plot the data
fig, ax = plt.subplots(figsize=(10,10))
merged.plot(column='OC (0-20 cm)', marker='.', ax=ax)
ax.set_title('Average Organic Carbon Content (0-20 cm) by General Land Cover Type')
plt.savefig('plots/average_oc_by_land_cover.png')
