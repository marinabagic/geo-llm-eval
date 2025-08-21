
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

geo_df = gpd.read_file('geo_df.gpkg')
europe = gpd.read_file('europe.gpkg')

fig, ax = plt.subplots(figsize=(10,10))
europe.plot(ax=ax, color='lightgrey', marker='.', alpha=0.5)

# Assuming 'pH_H2O' is the column for soil pH in water
general_land_covers = geo_df['LC0_Desc'].unique()
average_ph_per_lc = {}

for lc in general_land_covers:
    land_cover_df = geo_df[geo_df['LC0_Desc'] == lc]
    if not land_cover_df.empty:
        average_ph_per_lc[lc] = land_cover_df['pH_H2O'].mean()

max_ph = max(average_ph_per_lc, key=average_ph_per_lc.get)
print(max_ph)
