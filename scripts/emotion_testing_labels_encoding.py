import pandas as pd

# Read the testing_labels.csv file
testing_labels = pd.read_csv('testing_labels.csv')

# Define a dictionary for label encoding
emotion_to_label = {
    'neutral': 0,
    'anger': 1,
    'happiness': 2,
    'disgust': 3,
    'anxiety': 4,
    'boredom': 5,
    'sadness': 6
}

# Encode the emotions column
testing_labels['emotion_encoded'] = testing_labels['emotion'].map(emotion_to_label)

# Print the encoded labels
print(testing_labels)
