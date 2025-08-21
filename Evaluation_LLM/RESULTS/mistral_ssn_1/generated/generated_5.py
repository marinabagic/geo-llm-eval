
import pandas as pd
import geopandas as gpd

europe_shapefile = gpd.read_file('europe.gpkg')
europe_shapefile['color'] = 'lightgrey'

geo_df = pd.read_csv('LUCAS.csv')
south_eu = ['PT', 'ES', 'IT', 'GR', 'MT', 'HR', 'SI', 'CY']
south_eu_df = geo_df[geo_df['NUTS_0'].isin(south_eu)]
average_pH_CaCl2_south_eu = south_eu_df['pH_CaCl2'].mean()
print(average_pH_CaCl2_south_eu)

# Save the Europe shapefile to a GeoDataFrame
europe_geo_df = gpd.GeoDataFrame(geometry=europe_shapefile['geometry'], crs=europe_shapefile.crs)

# Plot Europe shapefile with lightgrey color
europe_geo_df.plot(color='lightgrey', marker='.', figsize=(10,10))
