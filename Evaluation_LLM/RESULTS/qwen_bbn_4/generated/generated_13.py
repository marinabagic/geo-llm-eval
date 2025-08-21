
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('LUCAS.csv')

# Filter for carbonate content in the top 20 cm
carbonate_content = df[df['Depth'] == '0-20 cm']['CaCO3']

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(carbonate_content, bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Carbonate Content (0-20 cm)')
plt.xlabel('Carbonate Content')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('plots/plot13.png')
plt.close()
