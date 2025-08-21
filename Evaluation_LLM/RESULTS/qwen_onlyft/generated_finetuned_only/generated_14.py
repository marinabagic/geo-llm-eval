
import pandas as pd

df = pd.read_file("geo_df.gpkg")
result = df.groupby("LC")["N"].mean().reset_index()
result.columns = ["General_Land_Cover", "Average_Nitrogen"]
print(result)
