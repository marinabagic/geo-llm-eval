
import pandas as pd
import scipy.stats as stats

df = pd.read_csv('LUCAS.csv')
df['EC_zscore'] = stats.zscore(df['EC'], nan_policy='omit')
outliers = df[(df['EC_zscore'] > 3) | (df['EC_zscore'] < -3)]
outliers.to_csv('LUCAS_EC_outliers.csv', index=False)
