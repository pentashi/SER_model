import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('normalized_features.csv')

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Display summary statistics
print("\nSummary statistics of the DataFrame:")
print(df.describe())

# Check for missing values
print("\nNumber of missing values in each column:")
print(df.isnull().sum())
