
import pandas as pd

# Load the data
df = pd.read_csv("LUCAS.csv")

# Group by land cover class and calculate the mean pH in water
mean_pH = df.groupby('LC0_Desc')['pH_H2O'].mean()

# Find the land cover class with the highest average pH in water
highest_pH_class = mean_pH.idxmax()

print(highest_pH_class)
