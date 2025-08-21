
import pandas as pd
import scipy.stats as stats

df = pd.read_csv('LUCAS.csv')
df = df.dropna(subset=['N', 'Country'])

austria_n = df[(df["Country"] == "Austria") & df["N"].notna()]["N"]
france_n = df[(df["Country"] == "France") & df["N"].notna()]["N"]

t_stat, p_value = stats.ttest_ind(austria_n, france_n)
print("T-statistic:", t_stat)
print("P-value:", p_value)
