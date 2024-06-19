import os
from parse_file_names import parse_file_name

# Directory containing the WAV files
directory = 'C:\\Users\\ACHAPI-STATION\\Desktop\\wav'

# Create a dictionary to store emotion labels for each file
emotion_labels = {}

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.wav'):
        # Parse file name to extract emotion label
        emotion_label = parse_file_name(filename)

        # Store emotion label in the dictionary with the file name as key
        emotion_labels[filename] = emotion_label

# Save file names and corresponding emotion labels to a single file
with open('emotion_labels.txt', 'w') as emotion_file:
    for filename, label in emotion_labels.items():
        emotion_file.write(f"{filename}: {label}\n")
