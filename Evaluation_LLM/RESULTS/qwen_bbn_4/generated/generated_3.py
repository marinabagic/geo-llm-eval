
import pandas as pd
from scipy.stats import ttest_ind

# Load the LUCAS dataset
df = pd.read_csv('LUCAS.csv')

# Filter data for Austria and France
austria_data = df[df['NUTS_0'] == 'AT']['N']
france_data = df[df['NUTS_0'] == 'FR']['N']

# Perform t-test
t_statistic, p_value = ttest_ind(austria_data, france_data)

# Print results
print(f"T-statistic: {t_statistic}, p-value: {p_value}")
