
import pandas as pd

# Load the dataframe
df = pd.read_csv("LUCAS_with_country_info.csv")

# Convert 'K' to numeric
df["K"] = pd.to_numeric(df["K"], errors="coerce")

# Group by NUTS_2 and calculate the mean potassium for each region
nuts2_k_mean = df.groupby("NUTS_2")["K"].mean().sort_values(ascending=False)

# Get the top 3 regions with the highest potassium
top_3_regions = nuts2_k_mean.head(3)

# Print the top 3 regions
print(top_3_regions)
