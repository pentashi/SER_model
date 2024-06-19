import numpy as np
from sklearn.model_selection import train_test_split

# Load normalized features and emotion labels
normalized_features = np.loadtxt('normalized_features.csv', delimiter=',')
emotion_labels = np.genfromtxt('emotion_labels.txt', dtype=str)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(normalized_features, emotion_labels, test_size=0.2, random_state=42)

# Save the training and testing datasets
np.savetxt('training_features.csv', X_train, delimiter=',')
np.savetxt('testing_features.csv', X_test, delimiter=',')
np.savetxt('training_labels.csv', y_train, delimiter=',', fmt='%s')
np.savetxt('testing_labels.csv', y_test, delimiter=',', fmt='%s')

print("Training features shape:", X_train.shape)
print("Testing features shape:", X_test.shape)
print("Training labels shape:", y_train.shape)
print("Testing labels shape:", y_test.shape)
