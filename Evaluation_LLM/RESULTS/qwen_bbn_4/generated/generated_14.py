
import pandas as pd

# Load the data
df = pd.read_csv('LUCAS.csv')

# Group by general land cover class and calculate average nitrogen
average_nitrogen = df.groupby('LC0_Desc')['N'].mean()

print(average_nitrogen)
