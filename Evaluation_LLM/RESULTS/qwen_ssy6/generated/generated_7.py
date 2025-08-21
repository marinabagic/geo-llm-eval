
import pandas as pd

df = pd.read_csv('LUCAS.csv')
top_regions = df.groupby('NUTS_2')['K'].mean().nlargest(3)
print(top_regions)
