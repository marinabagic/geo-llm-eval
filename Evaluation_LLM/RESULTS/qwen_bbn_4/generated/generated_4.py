
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('LUCAS.csv')

# Plot histogram of phosphorus content with KDE
plt.figure(figsize=(10, 6))
plt.hist(df['P'], bins=30, density=True, alpha=0.6, color='g', label='Histogram')
plt.kdeplot(df['P'], color='r', label='KDE')
plt.xlabel('Phosphorus Content')
plt.ylabel('Density')
plt.title('Histogram of Phosphorus Content with KDE')
plt.legend()
plt.savefig('plots/plot4.png')
plt.close()
