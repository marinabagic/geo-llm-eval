
import pandas as pd

# Load the LUCAS dataset
df = pd.read_csv('LUCAS.csv')

# Define the list of southern European countries
south_eu = ['PT', 'ES', 'IT', 'GR', 'MT', 'HR', 'SI', 'CY']

# Filter the dataset for southern European countries
south_eu_df = df[df['NUTS_0'].isin(south_eu)]

# Calculate the average pH in calcium chloride for southern European countries
avg_ph_cacl2 = south_eu_df['pH_CaCl2'].mean()

# Print the average pH
print(avg_ph_cacl2)
