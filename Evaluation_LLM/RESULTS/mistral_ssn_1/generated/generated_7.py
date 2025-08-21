
import pandas as pd

df = pd.read_csv("LUCAS.csv")
grouped = df.groupby('NUTS_2')['K'].mean().sort_values(ascending=False)
print(grouped.head(3))
