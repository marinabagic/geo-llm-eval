
import pandas as pd

df = pd.read_csv('LUCAS.csv')
average_nitrogen = df.groupby('LC')['N'].mean().reset_index()
print(average_nitrogen)
