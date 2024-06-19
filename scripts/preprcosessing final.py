import pandas as pd

# Read the CSV file
data = pd.read_csv('joined_data.csv', header=None)

# Exclude numeric columns from splitting
numeric_columns = [0, 1, 2]  # Adjust column indices based on your data
numeric_data = data.iloc[:, numeric_columns]
label_and_features = data.drop(columns=numeric_columns)

# Convert the remaining data to string
label_and_features = label_and_features.astype(str)

# Split the last column into features and label
label_and_features = label_and_features.iloc[:, 0].str.split(',', expand=True)

# Combine numeric data with label and features
preprocessed_data = pd.concat([numeric_data, label_and_features], axis=1)

# Save the preprocessed data
preprocessed_data.to_csv('preprocessed_data.csv', index=False)
