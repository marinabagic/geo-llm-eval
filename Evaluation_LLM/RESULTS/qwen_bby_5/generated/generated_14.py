
import pandas as pd

df = pd.read_csv('LUCAS.csv')
df["LC0_Desc"] = df["LC0_Desc"].fillna("Unknown")
avg_n_per_lc = df.groupby("LC0_Desc")["N"].mean().reset_index()
print(avg_n_per_lc)
