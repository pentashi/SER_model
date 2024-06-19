import pandas as pd

# Load features from CSV file
features_df = pd.read_csv('normalized_features.csv', header=None)

# Extract labels (first value in each row) and features (remaining values in each row)
labels = features_df.iloc[:, 0]  # First column contains labels
features = features_df.iloc[:, 1:]  # Remaining columns contain features

# Check the first few labels
print(labels.head())

# Check the first few rows of features
print(features.head())
