
import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv('LUCAS.csv')
austria_nitrogen = df[(df["NUTS_0"] == "AT") & (df["N"].apply(lambda x: isinstance(x, (int, float))))]["N"]
france_nitrogen = df[(df["NUTS_0"] == "FR") & (df["N"].apply(lambda x: isinstance(x, (int, float))))]["N"]

t_statistic, p_value = ttest_ind(austria_nitrogen, france_nitrogen)
print(f"T-statistic: {t_statistic}, p-value: {p_value}")
