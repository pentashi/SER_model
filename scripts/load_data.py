import pandas as pd

# Load emotion labels
emotion_labels_path = "C:\\Users\\ACHAPI-STATION\\PycharmProjects\\SER\\scripts\\emotion_labels.txt"
emotion_labels_df = pd.read_csv(emotion_labels_path, header=None, names=["filename", "emotion"])

# Load normalized features
normalized_features_path = "C:\\Users\\ACHAPI-STATION\\PycharmProjects\\SER\\scripts\\normalized_features.csv"
normalized_features_df = pd.read_csv(normalized_features_path, header=None)

# Confirm data loading
print("Emotion labels shape:", emotion_labels_df.shape)
print("Normalized features shape:", normalized_features_df.shape)
