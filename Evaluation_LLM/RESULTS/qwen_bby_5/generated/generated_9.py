
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway

# Load data
df = pd.read_csv("LUCAS_with_country_info.csv")
df = df.dropna(subset=["OC", "LC0_Desc"])

# Group by land cover and calculate mean OC
oc_by_lc = df.groupby("LC0_Desc")["OC"].mean().reset_index()

# ANOVA test
anova_result = f_oneway(*[group["OC"] for name, group in df.groupby("LC0_Desc")])
p_value = anova_result.pvalue

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x="OC", y="LC0_Desc", data=oc_by_lc, ax=ax)
ax.set_title(f"Organic Carbon Content by Land Cover (p-value: {p_value:.4f})")
ax.set_xlabel("Mean Organic Carbon (%)")
ax.set_ylabel("Land Cover Category")

plt.tight_layout()
plt.savefig('plots/plot9.png')
plt.close()
