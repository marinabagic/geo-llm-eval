
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("LUCAS_with_country_info.csv")
df["EC"] = pd.to_numeric(df["EC"], errors="coerce")
df = df.dropna(subset=["LU_DESC", "EC"])

plt.figure(figsize=(12, 8))
df.boxplot(column="EC", by="LU_DESC", vert=False)
plt.suptitle("")
plt.title("Boxplot of EC by Land Use Class")
plt.xlabel("EC")
plt.ylabel("Land Use Class")
plt.tight_layout()
plt.savefig('plots/plot8.png')
plt.close()
