import csv

# Read normalized features from CSV
data_list = []
with open('normalized_features.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data_list.append(row)

# Read emotion labels from text file
label_mapping = {'happiness': 0, 'anger': 1, 'sadness': 2, 'disgust': 3, 'boredom': 4, 'anxiety': 5, 'neutral': 6}
labels = []
with open('emotion_labels.txt', 'r') as file:
    for line in file:
        filename, emotion = line.strip().split(': ')
        labels.append(label_mapping[emotion])

# Join labels with normalized features
for i in range(len(data_list)):
    data_list[i].append(labels[i])

# Save joined data to a new CSV file
with open('joined_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data_list)

print("Joined data saved to joined_data.csv")
