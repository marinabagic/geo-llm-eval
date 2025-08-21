
import pandas as pd

df = pd.read_csv("LUCAS.csv")
result = df.groupby('LC0_Desc')['pH_H2O'].mean().idxmax()
print(result)
