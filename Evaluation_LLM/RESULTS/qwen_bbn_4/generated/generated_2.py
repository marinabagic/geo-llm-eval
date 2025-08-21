
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load LUCAS data
df = pd.read_csv('LUCAS.csv')

# Calculate average organic carbon content by general land cover type
avg_oc_by_lc = df.groupby('LC')['OC'].mean().reset_index()

# Create a bar plot
fig, ax = plt.subplots(figsize=(10, 10))
plt.bar(avg_oc_by_lc['LC'], avg_oc_by_lc['OC'], color='skyblue')
plt.xlabel('General Land Cover Type')
plt.ylabel('Average Organic Carbon Content (0-20 cm)')
plt.title('Average Organic Carbon Content by General Land Cover Type')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('plots/plot2.png')
