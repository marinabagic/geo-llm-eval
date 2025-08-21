
import pandas as pd

df = pd.read_csv('LUCAS.csv')
south_eu = ['PT', 'ES', 'IT', 'GR', 'MT', 'HR', 'SI', 'CY']
south_eu_df = df[df['NUTS_0'].isin(south_eu)]
avg_ph = south_eu_df['pH_CaCl2'].mean()
print(avg_ph)
