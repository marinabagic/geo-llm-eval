
import pandas as pd

df = pd.read_csv("LUCAS_with_country_info.csv")
df["K"] = pd.to_numeric(df["K"], errors="coerce")
df = df.dropna(subset=["K", "NUTS_2"])
top_regions = df.groupby("NUTS_2")["K"].mean().nlargest(3)
print(top_regions)
