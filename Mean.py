import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
dataset = sns.load_dataset('iris')

# Calculate means
overall_means = dataset.select_dtypes(include=[np.number]).mean()
species_means = dataset.groupby('species').mean()

print("OVERALL MEANS:")
print(overall_means)

print("\nMEANS BY SPECIES:")
print(species_means)

# Visualize the means
plt.figure(figsize=(10, 6))

# Overall means plot
plt.subplot(1, 2, 1)
overall_means.plot(kind='bar', color='skyblue')
plt.title('Overall Mean of Iris Features')
plt.ylabel('Mean Value (cm)')
plt.xticks(rotation=45)

# Species means plot
plt.subplot(1, 2, 2)
species_means.T.plot(kind='bar')  # Transpose for better visualization
plt.title('Mean Values by Species')
plt.ylabel('Mean Value (cm)')
plt.xticks(rotation=45)
plt.legend(title='Species')

plt.tight_layout()
plt.show()

# Detailed statistical summary
print("\n📈 DETAILED STATISTICAL SUMMARY:")
print(dataset.describe())