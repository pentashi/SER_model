def transform_emotions(input_file, output_file):
    emotions = []

    # Read input file and extract emotions
    with open(input_file, 'r') as file:
        for line in file:
            # Split the line by ":" and take the second part (emotion)
            emotion = line.split(":")[-1].strip()
            emotions.append(emotion)

    # Write emotions to output file
    with open(output_file, 'w') as file:
        for emotion in emotions:
            # Write each emotion surrounded by single quotes and separated by a comma
            file.write(f"'{emotion}',\n")

# Example usage:
input_file = "emotion_labels.txt"
output_file = "output.txt"
transform_emotions(input_file, output_file)
