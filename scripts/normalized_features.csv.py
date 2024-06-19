import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('normalized_features.csv')

# Plot histograms for all features using Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(15, 10))
for i, column in enumerate(data.columns):
    plt.subplot(4, 4, i + 1)
    sns.histplot(data[column], bins=20, kde=True)
    plt.title(column)
plt.tight_layout()
plt.show()
