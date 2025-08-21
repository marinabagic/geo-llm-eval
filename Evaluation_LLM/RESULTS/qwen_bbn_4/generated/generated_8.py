
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("LUCAS_with_country_info.csv")

# Group by land use class and create boxplot for EC
plt.figure(figsize=(12, 8))
df.boxplot(column='EC', by='LC0_Desc', grid=False)
plt.suptitle('Boxplot of EC grouped by Land Use Class')
plt.title('')
plt.xlabel('Land Use Class')
plt.ylabel('EC')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('plots/plot8.png')
