import csv

def read_labels_from_csv(file_path):
    labels = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:  # Ensure that the row has two values
                audio_file_name, label = row[0].strip(), row[1].strip()  # Remove any leading/trailing whitespaces
                labels[audio_file_name] = label
            else:
                print(f"Ignoring invalid row: {row}")
    return labels

# Example usage
training_labels_file = "training_labels.csv"
training_labels = read_labels_from_csv(training_labels_file)
print(training_labels)
